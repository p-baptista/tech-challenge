from typing import List, Optional
from fastapi import HTTPException
from pydantic import UUID4

from repository.user_repository import UserRepository
from schemas.user_schema import User

class UserService:
    def __init__(self) -> None:
        self.repository = UserRepository()

    def get_by_id(self, _cpf: int) -> User:
        return self.repository.get_by_cpf(_cpf)