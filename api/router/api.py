from fastapi import APIRouter
from router.v1 import user

router = APIRouter(
    prefix="/api/v1"
)

router.include_router(user.router)