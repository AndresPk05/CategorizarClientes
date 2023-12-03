from pydantic import BaseModel

class Client(BaseModel):
   id: int
   gender: str
   age: int
   annualIncome: int
   score: int