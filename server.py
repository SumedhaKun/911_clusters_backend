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
# Load the pre-trained word vectors model
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
   nltk.download('wordnet')
   file_contents = []
   file_dict={}
   stop_words = set(stopwords.words('english'))
   # Iterate over each uploaded file
   for index,file in enumerate(files):
       # Read the file contents as bytes
       file_bytes = await file.read()
          
       # Decode the bytes into a string
       file_string = file_bytes.decode('utf-8')
       # Append the string to the list
       document=re.sub(r'\W', ' ', str(file_string))
       document = re.sub(r'\^[a-zA-Z]\s+', ' ', document)
       document = re.sub(r'\s+', ' ', document, flags=re.I)
       document = re.sub(r'^b\s+', '', document)
       document = re.sub(r'[^\w\s]', '', document)
       document = document.lower()
       document = document.split()
       document = [stemmer.lemmatize(word) for word in document]
       document = ' '.join(document)
       document = word_tokenize(document)
       document = [w for w in document if not w.lower() in stop_words]
       document=' '.join(document)
       file_contents.append(embed_string(document))
       file_dict[embed_string(document)[0]]=index
  
   num_clusters = 3
   kmeans = KMeans(n_clusters=num_clusters)
  
   
   X=np.array(file_contents)
   kmeans.fit(X)
   cluster_labels = kmeans.labels_
   plt.scatter(X[:, 0], X[:, 1], c=cluster_labels, cmap='viridis')
   plt.xlabel('Crime feature #2')
   plt.ylabel('Crime feature #1')
   plt.title('Clustering Results')
   plt.colorbar(label='Cluster')
   i=0
   for (xi, yi) in zip(X[:, 0], X[:, 1]):
      val=str(file_dict.get(X[i][0],0))
      plt.text(xi, yi, val, va='bottom', ha='center')
      i+=1
   plt.show()
   bytes_image = io.BytesIO()
   plt.savefig(bytes_image, format='png')
   bytes_image.seek(0)
   encoded_img = base64.b64encode(bytes_image.getvalue()).decode()
   return encoded_img
       
def embed_string(text):
   # Tokenize the string
   tokens = nlp(text)
   # Average the word vectors to get a single vector representation for the string
   vector = sum(token.vector for token in tokens) / len(tokens)
   return vector
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



