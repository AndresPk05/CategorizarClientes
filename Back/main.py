from typing import List
from fastapi import FastAPI
from modelo import KMeansModel
from client import Client
from fastapi.middleware.cors import CORSMiddleware
import utils

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/train")
def train_model(data: List[Client]):
    jsonData=utils.transformData(data)
    model = KMeansModel()
    prediction = model.predict(jsonData)
    return prediction