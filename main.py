from fastapi import FastAPI

app = FastAPI()

@app.post("/dogrecognition")
def recognizedog():
    return {"Hello world"}


