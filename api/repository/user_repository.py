from fastapi import HTTPException
from pydantic import TypeAdapter
import requests

from schemas.user_schema import User

class UserRepository:
    def get_by_cpf(self, _cpf) -> User:
            request = requests.get(f"http://localhost:8001/users/{_cpf}")

            if request.status_code == 503:
                request = requests.get(f"http://localhost:8002/users/{_cpf}")
            
            request.raise_for_status()

            user = TypeAdapter(User).validate_json(request.text)
            return user