from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from typing import List
import uvicorn
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
    res=[]
    for file in files:
        res.append(file.file)
    return {'message': res}

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

'''
document = re.sub(r'\W', ' ', str(X[sen]))
        
        # remove all single characters
        document = re.sub(r'\s+[a-zA-Z]\s+', ' ', document)
        
        # Remove single characters from the start
        document = re.sub(r'\^[a-zA-Z]\s+', ' ', document) 
        
        # Substituting multiple spaces with single space
        document = re.sub(r'\s+', ' ', document, flags=re.I)
        
        # Removing prefixed 'b'
        document = re.sub(r'^b\s+', '', document)
        
        # Converting to Lowercase
        document = document.lower()
        
        # Lemmatization
        document = document.split()

        document = [stemmer.lemmatize(word) for word in document]
        document = ' '.join(document)
        
        documents.append(document)


        from sklearn.feature_extraction.text import TfidfVectorizer
        tfidfconverter1 = TfidfVectorizer(max_features=1500, min_df=5, max_df=0.7, stop_words=stopwords.words('english'))
        X = tfidfconverter1.fit_transform(documents).toarray()

'''
