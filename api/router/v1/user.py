from typing import List
from fastapi import APIRouter
from pydantic import UUID4

from schemas.user_schema import User
from service.user_service import UserService

router = APIRouter(
    prefix="/user",
)

@router.get("/{user_cpf}", status_code=200, response_model=User)
def get_by_id(user_cpf: int):
    _service = UserService()
    return UserService().get_by_id(user_cpf)