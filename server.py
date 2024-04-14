from fastapi import FastAPI, UploadFile
from pydantic import BaseModel
import uvicorn

app = FastAPI()


@app.post("/post/")
async def read_root(file:UploadFile):
    return {"message": file.filename}

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