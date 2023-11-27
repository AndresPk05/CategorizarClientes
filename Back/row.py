from pydantic import BaseModel

class Row(BaseModel):
    x: int
    y: str
    label: int