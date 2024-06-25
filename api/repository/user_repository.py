from pydantic import TypeAdapter
from fastapi import HTTPException
import requests

from schemas.user_schema import User
from config.constants import mockAPIs

class UserRepository:
    def get_by_cpf(self, _cpf) -> User:
        try:
            request = requests.get(f"{mockAPIs['cheap_api_route']}users/{_cpf}")

            # try accessing premium API, if cheap is unavailable
            if request.status_code == 503:
                request = requests.get(f"{mockAPIs['premium_api_route']}users/{_cpf}")
            
            request.raise_for_status()
        except:
            raise HTTPException(status_code=request.status_code)

        user = TypeAdapter(User).validate_json(request.text)
        return user