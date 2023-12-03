from client import Client
from typing import List
import json

def transformData(clients: List[Client]):
    data = []
    for client in clients:
        row = {
            "id": client.id,
            "gender": client.gender,
            "age": client.age,
            "annualIncome": client.annualIncome,
            "score": client.score
        }

        data.append(row)
    jsonData = json.dumps(data)
    return jsonData