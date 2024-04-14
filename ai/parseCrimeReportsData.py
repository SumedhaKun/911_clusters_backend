from langchain.embeddings import BedrockEmbeddings
import dbconnection
import numpy as np
import json
import psycopg2

conn = dbconnection.open_connection_to_db("rds!cluster-37ab34ae-e03e-4681-ad30-a7dfb19f2520")


def checkProcessedCaseFiles():
    try:
        with open("processedCaseFiles.txt", 'r') as file:
            # Read each line, strip whitespace, and convert directly to an integer
            integer_list = [int(line.strip()) for line in file]

        # Convert the list of integers to a numpy array
        return np.array(integer_list)

    except FileNotFoundError:
        print(f"The file 'prompt.txt' was not found.")

def generateVectorEmbedding(text):
    #create an Amazon Titan Text Embeddings client
    embeddings_client = BedrockEmbeddings(region_name="us-west-2")

    #Invoke the embedding model
    embedding = embeddings_client.embed_query(text)
    return(embedding)


def generateDBEntries(prompt):

    # pass the prompt to Claude 3 Sonnet

    # parse integers, characters, and other categorical/quantitative data from the output

    # pass the natural language features to the vector embedding function

    # recombine the vectorizations with the categorical/quantitative data from the output into a DB entry

    # return the parsed DB entries as a 2D list of feature embeddings/parsings

    return 0


def insertRecordIntoDB(table, record, conn):

    # Dynamically generates and executes an INSERT SQL statement for PostgreSQL, handling
    # special data types like datetime objects and arrays directly.
    
    # Args:
    # - table_name (str): The name of the table into which the record will be inserted.
    # - data (dict): A dictionary representing the record to be inserted, where keys are column names
    #                  and values can include native PostgreSQL types like datetime and arrays.
    # - conn (psycopg2.connection): A psycopg2 connection object.
    
    # Generate column names and placeholders
    columns = ', '.join(record.keys())
    placeholders = ', '.join(['%s'] * len(record))  # PostgreSQL uses %s as placeholder

    # Create the INSERT INTO statement
    sql = f'INSERT INTO {table} ({columns}) VALUES ({placeholders})'
    #print("columns=", columns)
    #print("placeholders=", placeholders)
    #print(sql)
    try:
        cur = conn.cursor()
        
        cur.execute(sql, tuple(record.values()))
        conn.commit()
        print("Record inserted successfully.")
    except psycopg2.Error as e:
        print("An error occurred:", e)

# Add a new database entry to the DB for processing
def addNewDBEntry(table, record, text):
    try:
        # get the base prompt
        with open("prompt.txt", "r") as promptFile:
            prompt = promptFile.readlines()
        print(prompt)

        prompt += text

        # create a new DB entry based on the input prompt, casefile
        dbEntry = generateDBEntries(prompt)

        # add a new casefile entry to the DB
        insertRecordIntoDB(table, record, conn)

    except FileNotFoundError:
        print(f"The file 'prompt.txt' was not found.")


def main():
    processedCaseFiles = checkProcessedCaseFiles()


    # read in all case files to one very long string,
    #       with each delimited by the starting phrase "################## START OF FILE ##################"
    #       and terminated with the phrase "################## END OF FILE ##################"
    caseFiles = ""
    for i in range(1, 465):
        # read a crime report into the case variable
        with open("crime-reports\\crime-report-" + str(i) + ".txt", "r") as crimeReport:
            case = crimeReport.readlines()

        print(case)
        caseFiles += "\n################## START OF FILE ##################\n" + case + "\n################## END OF FILE ##################\n"


    # get the base prompt
    with open("prompt.txt", "r") as promptFile:
        prompt = promptFile.readlines()
    print(prompt)


    # add the base prompt to the front of the input text
    prompt += caseFiles

    # create the parsed, vectorized DB entries for insertion
    dbEntries = generateDBEntries(prompt)

    with open("processedCaseFiles.txt", "w") as processedCaseFiles:
        processedCaseFiles.writelines(dbEntries)

    try:
        for caseFile in dbEntries:
            data_record = {}
            #  print(f"caseFile {caseFile}:")
            #  print(type(caseFile))
            # build data array for insert to vector DB
            # db columns: id, pubdate, title, linkurl, caseFiletext, contents
            data_record["caseNum"] = caseFile["caseNum"]

            #print(data_record)

            if int(data_record["caseNum"]) in processedCaseFiles:
                print(f"caseFile {data_record['id']} already processed.")
                continue

            else:
                data_record["crimeType"] = generateVectorEmbedding(caseFile["crimeType"])
                data_record["date"] = caseFile["date"]
                data_record["time"] = caseFile["time"]
                data_record["location"] = generateVectorEmbedding(caseFile["location"])
                data_record["victimName"] = generateVectorEmbedding(caseFile["victimName"])
                data_record["victimAge"] = caseFile["victimAge"]
                data_record["victimRelation"] = generateVectorEmbedding(caseFile["victimRelation"])
                data_record["eventSequence"] = generateVectorEmbedding(caseFile["eventSequence"])
                data_record["compromiseMethod"] = caseFile["compromiseMethod"]
                # 0 = female, 1 = male
                data_record["suspectSex"] = caseFile["suspectSex"]
                data_record["suspectRace"] = generateVectorEmbedding(caseFile["suspectRace"])
                data_record["suspectHeight"] = caseFile["suspectHeight"]
                data_record["suspectBuild"] = generateVectorEmbedding(caseFile["suspectBuild"])
                data_record["suspectClothes"] = generateVectorEmbedding(caseFile["suspectClothes"])
                data_record["tools"] = generateVectorEmbedding(caseFile["tools"])
                data_record["forceUsed"] = generateVectorEmbedding(caseFile["forceUsed"])
                data_record["weapon"] = generateVectorEmbedding(caseFile["weapon"])
                data_record["victimHarm"] = generateVectorEmbedding(caseFile["victimHarm"])
                data_record["itemsStolen"] = generateVectorEmbedding(caseFile["itemsStolen"])
                data_record["fundsStolen"] = caseFile["fundsStolen"]
                data_record["evidence"] = generateVectorEmbedding(caseFile["evidence"])
                data_record["suspectTechniques"] = generateVectorEmbedding(caseFile["suspectTechniques"])
                # 0 = closed, 1 = open
                data_record["status"] = caseFile["status"]
                data_record["notes"] = generateVectorEmbedding(caseFile["notes"])

                insertRecordIntoDB("case", data_record, conn)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    main()

# Special thanks to Darren Kraker for his help with getting this part of the project running