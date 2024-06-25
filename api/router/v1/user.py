from fastapi import APIRouter

from schemas.user_schema import User
from service.user_service import UserService

router = APIRouter(
    prefix="/user",
)

@router.get("/{user_cpf}", status_code=200, response_model=User)
def get_by_id(user_cpf: int):
    return UserService().get_by_cpf(user_cpf)