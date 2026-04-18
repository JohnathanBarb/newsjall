from fastapi import APIRouter

from src.users.schemas import CreateUserInput, CreateUserOutput

users_router = APIRouter()


@users_router.post(
    "",
    response_model=CreateUserOutput,
)
async def create_user(create_user_payload: CreateUserInput):
    return
