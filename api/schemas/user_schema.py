from pydantic import BaseModel

# user data structure found in mock APIs
class User(BaseModel):
    cpf: int
    name: str
    age: int

    class ConfigDict:
        from_attributes = True