from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from typing import List
import uvicorn
import base64
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import io
import numpy as np
import re
from nltk.corpus import stopwords
import nltk
from nltk.stem import WordNetLemmatizer
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
import spacy
import json
import cluster_functions


nlp = spacy.load("en_core_web_sm")
import ssl
from nltk.tokenize import word_tokenize
try:
   _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
   pass
else:
   ssl._create_default_https_context = _create_unverified_https_context
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('punkt')
stemmer=WordNetLemmatizer()
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
origins = [
   "*"
]
app.add_middleware(
   CORSMiddleware,
   allow_origins=origins,
   allow_methods=["*"],
   allow_credentials=True,
   allow_headers=['*'])
class FormList(BaseModel):
   data:List[UploadFile]
@app.post("/post/")
async def read_root(files:List[UploadFile]):
   df=await cluster_functions.extract_features(files)
   df= cluster_functions.tokenize_and_embed(df)

   crime_img=cluster_functions.cluster(df,3,"CRIME")
   method_img=cluster_functions.cluster(df,4,"METHOD")
   evidence_img=cluster_functions.cluster(df,5,"EVIDENCE")
   return [crime_img,method_img,evidence_img]


if __name__ == "__main__":
   import asyncio
   import nest_asyncio
   nest_asyncio.apply()  # Allows running asyncio code in Jupyter Notebook or similar environments
   loop = asyncio.get_event_loop()
   loop.create_task(uvicorn.run(app, host="127.0.0.1", port=8000))
   try:
       loop.run_forever()
   except KeyboardInterrupt:
       pass
   finally:
       loop.close()



