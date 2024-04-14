import time
import boto3
import os
import numpy as np
import traceback
import psycopg2
import requests
import json
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.chat_models import BedrockChat
from langchain_community.llms import Bedrock
from langchain_community.embeddings import BedrockEmbeddings
import dbconnection  # Assuming this module handles database connections


def read_and_clean_file(file_path):
    """
    Reads a file from the given path, cleans up extra white spaces,
    and escapes double quotes.

    :param file_path: Path to the file to be read.
    :return: A cleaned and escaped string containing the file's content.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            # Strip leading and trailing whitespaces then replace double quotes with escaped double quotes
            cleaned_content = ' '.join(content.split()).replace('"', '\\"')
            return cleaned_content
    except Exception as e:
        return f"Error reading file: {e}"


def generate_hyde_response(query):
    bedrock = Bedrock(
        model_id="anthropic.claude-3-sonnet-20240229-v1:0",
        model_kwargs={
            "temperature": 0.7,
            "max_tokens_to_sample": 1000,
            "top_p": 0.9,
        },
    )
    try:
        # Define the prompt template
        template = "You are a helpful assistant. Given the following question \n {query} can you please generate a fictitious news article about that answers the question."
        prompt = ChatPromptTemplate.from_template(template)

        # Format the prompt with the user's query
        formatted_prompt = prompt.format_prompt(query=query)

        # Extract the content of the formatted prompt
        message_content = formatted_prompt.to_messages()[0].content

        # Send the message content to Claude using Bedrock and get the response
        response = bedrock.generate([message_content])
        result = json.loads(response.get("body").read())
        output_list = result.get("content", [])
        print(f"- The model returned {len(output_list)} response(s):")
        for output in output_list:
            print(output["text"])

        return result
    except Exception as e:
        exc_type, exc_value, exc_traceback = traceback.sys.exc_info()
        line_number = exc_traceback.tb_lineno

        return f"ERROR generating HyDe response: {exc_type}{exc_value}{exc_traceback} on {line_number}"


def calculate_zscores(cosine_scores):
    zscores = []
    # Calculate the mean of the sample points
    mean = np.mean(cosine_scores)
    # Calculate the standard deviation of the sample points
    std_deviation = np.std(cosine_scores, ddof=1)  # ddof=1 for sample standard deviation
    # Calculate the z-scores for each sample point
    z_scores = [(x - mean) / std_deviation for x in cosine_scores]

    return z_scores


def run_similarity_search_pgvector(num_records, question, embedded_text, conn):
    sql = f"SELECT id, title, articletext, 1-(contents <=> ('{embedded_text}')) as cosine_similar \
            FROM public.story \
            ORDER BY cosine_similar DESC \
            LIMIT {num_records}"
    cosine_scores = []
    try:
        article_text = ""
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()

        # grab all the cosine scores so we can compute Z score for narrow article selection
        for row in rows:
            cosine_scores.append(row[3])

        # Close cursor and connection
        cur.close()
        cleaned_content = ' '.join(article_text.split()).replace('"', '\\"')
        print("A:" + best_answer(cleaned_content, question))

    except psycopg2.Error as e:
        print("An error occurred:", e)


def run_similarity_search_opensearch(num_records, question):
    url = 'https://pweqpdrhja.execute-api.us-east-1.amazonaws.com/prod/api/aoss/search'
    api_key = "9|ge;ZN[5E*W$EO.6h6Z<oHQT+X9*b5W"  # os.getenv('x-api-key')
    headers = {
        'x-api-key': api_key,
        'Content-Type': 'application/json',
    }
    data = {
        'user_input': question
    }

    response = requests.post(url, json=data, headers=headers)
    article_text = ""
    if response.status_code == 200:
        response_json = response.json()
        # print(response_json)
        if 'Search response' in response_json:
            hits = response_json['Search response']['hits']['hits']
            opensearch_scores = []
            for hit in hits:
                opensearch_scores.append(hit['_score'])

            z_scores = calculate_zscores(opensearch_scores)
            zscore_index = 0
            for hit in hits:

                if (z_scores[zscore_index] > 1):
                    print(
                        f"{hit['_source']['content-id']},\"{hit['_source']['content-title']}\",{hit['_score']},{z_scores[zscore_index]}")
                    article_text = article_text + hit['_source']['content-raw-cleaned'] + "\n"
                zscore_index += 1
            cleaned_content = ' '.join(article_text.split()).replace('"', '\\"')
            print("A:" + best_answer(cleaned_content, question))
        else:
            print("The response JSON does not contain a search response.")
    else:
        print(f"Failed to call API. Status code: {response.status_code}, Response: {response.text}")


def generate_vector_embedding(text):
    # create an Amazon Titan Text Embeddings client
    embeddings_client = BedrockEmbeddings(region_name="us-east-1")

    # Invoke the model
    embedding = embeddings_client.embed_query(text)
    return (embedding)


def best_answer(prompt, text, data, question):
    model_id = "anthropic.claude-3-sonnet-20240229-v1:0"

    model_kwargs = {
        "max_tokens": 2048,
        "temperature": 0.0,
        "top_k": 250,
        "top_p": 0.9,
        "stop_sequences": ["\n\nHuman"],
    }

    model = BedrockChat(
        client=bedrock_runtime,
        model_id=model_id,
        model_kwargs=model_kwargs,
    )

    human_prompt = "You are to answer the question using the data in the following article.  Do not make up your answer, only use \
                    supporting data from the article, If you don't have enough data simply respond, I don't have enough information to answer that question. \
                    given the following news article data {data} can you please give a concise answer to the following question. {question}"
    messages = [
        ("system", "You are a helpful assistant that can answer quesitons based on news articles you have been given."),
        ("human", human_prompt),
    ]
    try:
        prompt = ChatPromptTemplate.from_messages(messages)

        chain = prompt | model | StrOutputParser()

        # Chain Invoke
        start_time = time.time()  # Start timing
        # Call Bedrock
        response = chain.invoke({"data": data, "question": question})
        end_time = time.time()  # End timing
        print("Claude call took :", end_time - start_time)  # Calculate execution time

        return (response)
    except Exception as e:
        exc_type, exc_value, exc_traceback = traceback.sys.exc_info()
        line_number = exc_traceback.tb_lineno

        return f"ERROR generating good answer: {exc_type}{exc_value}{exc_traceback} on {line_number}"


def main():
    conn = dbconnection.open_connection_to_db("rds!cluster-aa22ca55-d570-453a-a0e5-1cf9c91ab902")

    with open("questions.txt", 'r') as file:
        # Read each line, strip whitespace, and convert directly to an integer
        for line in file:
            query = line.strip()
            print(f"Q(PGVECTOR): {query}")
            vec_embed = generate_vector_embedding(query)
            run_similarity_search_pgvector(15, query, vec_embed, conn)
            print(f"Q(OpenSearch): {query}")
            run_similarity_search_opensearch(5, query)

    conn.close()


if __name__ == "__main__":
    main()
