from pydantic import BaseModel

class User(BaseModel):
    cpf: int
    name: str
    age: int