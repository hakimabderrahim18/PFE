from pydantic import BaseModel
from typing import List

class Document(BaseModel):
    name: str

class Step(BaseModel):
    order: int
    description: str

class Intent(BaseModel):
    name: str
    utterances: List[str]

class Response(BaseModel):
    text: str

class Procedure(BaseModel):
    name: str
    documents: List[Document]
    steps: List[Step]
    intents: List[Intent]
    responses: List[Response]
