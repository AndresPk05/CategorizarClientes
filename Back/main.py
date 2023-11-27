from typing import List
from fastapi import FastAPI
from modelo import KMeansModel

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/train")
def train_model(data: str):
    return KMeansModel().predict(data)