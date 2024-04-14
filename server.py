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