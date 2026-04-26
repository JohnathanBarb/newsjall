from fastapi import APIRouter, Depends

from src.users.dependencies import get_user_service
from src.users.schemas import CreateUserInput, CreateUserOutput
from src.users.service import UserService

users_router = APIRouter()


@users_router.post(
    "",
    response_model=CreateUserOutput,
)
async def create_user(
    create_user_payload: CreateUserInput,
    service: UserService = Depends(get_user_service),
):
    return await service.create(create_user_payload)
