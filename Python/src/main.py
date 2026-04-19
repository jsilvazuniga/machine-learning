from fastapi import FastAPI
import debugpy  

app = FastAPI()


debugpy.listen(5678)
debugpy.wait_for_client()  # blocks execution until client is attached


@app.get("/")
def read_root():
    text = "Hello World! This is a FastAPI application running. "
    return {"message": text}