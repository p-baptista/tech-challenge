from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, TypeAdapter
from typing import List
import json, os, random

ERROR_CHANCE = 0.5

app = FastAPI()

class User(BaseModel):
    cpf: int
    name: str
    age: int

@app.post("/users/", response_model=User)
async def create_user(user: User):
    users.append(user)
    return user

@app.get("/users/", response_model=List[User])
async def read_all_users():
    return users

@app.get("/users/{user_cpf}", response_model=User)
async def read_user(user_cpf: int):
    if random.random() < ERROR_CHANCE:
        raise HTTPException(status_code=503, detail="Service Unavailable")

    for user in users:
        if user.cpf == user_cpf:
            return user
        
    raise HTTPException(status_code=404, detail="User not found")

@app.put("/users/{user_cpf}", response_model=User)
async def update_user(user_cpf: int, user_update: User):    
    for idx, user in enumerate(users):
        if user.cpf == user_cpf:
            updated_user = user.copy(update=user_update.model_dump(exclude_unset=True))
            users[idx] = updated_user
            return updated_user
    
    raise HTTPException(status_code=404, detail="User not found")

@app.delete("/users/{user_cpf}", response_model=User)
async def delete_user(user_cpf: int):
    for idx, user in enumerate(users):
        if user.cpf == user_cpf:
            return users.pop(idx)
        
    raise HTTPException(status_code=404, detail="User not found")

if __name__ == "__main__":
    import uvicorn

    seed_path = os.path.join(os.path.dirname(__file__), "seed.json")
    seed_file = open(seed_path)
    data = json.load(seed_file)

    adapter = TypeAdapter(List[User])
    users = adapter.validate_python(data)

    uvicorn.run(app, host="0.0.0.0", port=8001)