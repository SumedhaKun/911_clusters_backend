import spacy
import glob
import io
import pandas
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
import nltk
from sklearn.decomposition import PCA
from nltk.corpus import stopwords
from sklearn.preprocessing import StandardScaler
import numpy as np
import base64
nltk.download('stopwords')
embed_spacy=spacy.load('en_core_web_md')


async def extract_features(files)->pandas.DataFrame:
    nlp = spacy.load("models")
    dict_list=[]
    for file in files:
        obj={}
        file_bytes = await file.read()
        text = file_bytes.decode('utf-8')
        doc = nlp(text)
        for ent in doc.ents:
            obj[ent.label_]=ent.text
        dict_list.append(obj)
    df=pandas.DataFrame(dict_list)
    return df


def tokenize(text):
    if pandas.isnull(text):
        return []
    else:
        tokens= word_tokenize(text.lower())
        stop_words = set(stopwords.words('english'))  # Set of English stopwords
        return [word for word in tokens if word not in stop_words]
    
def embed(tokens):
    return [embed_spacy(word).vector for word in tokens]

def normalize(embeddings):
    norm = np.linalg.norm(embeddings)
    if norm == 0:
        return embeddings
    return embeddings / norm

def tokenize_and_embed(df)->pandas.DataFrame:
    tokenized_dict={"CASE_NUMBER":df["CASE_NUMBER"],"DATE":df["DATE"], "LOCATION":df["LOCATION"], "CRIME":df["CRIME"].apply(tokenize).apply(embed).apply(normalize), "METHOD":df["METHOD"].apply(tokenize).apply(embed).apply(normalize), "EVIDENCE": df["EVIDENCE"].apply(tokenize).apply(embed).apply(normalize)}
    return pandas.DataFrame(tokenized_dict)


# DBScan Clustering
def cluster( df, i,param):
    for index, row in df.iterrows():
        if len(row.iloc[i])==0:
            df.drop(index,inplace=True)
    df_exploded = df.explode(param)
    X = np.array(df_exploded[param].tolist())
    dbscan = DBSCAN(eps=0.4, min_samples=2)
    labels = dbscan.fit_predict(X)
    df_exploded['cluster_label'] = labels
    plt.figure(figsize=(8, 6))

    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X)

    # Plot points with different colors for each cluster and noise points
    unique_labels = np.unique(labels)
    for label in unique_labels:
        if label == -1:
            plt.scatter(X_pca[labels == label, 0], X_pca[labels == label, 1], color='gray', marker='x', label='Noise')
        else:
            plt.scatter(X_pca[labels == label, 0], X_pca[labels == label, 1], label=f'Cluster {label}')
    

    plt.title(param)
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.legend()
    plt.show()

    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png')
    bytes_image.seek(0)
    return base64.b64encode(bytes_image.getvalue()).decode()














