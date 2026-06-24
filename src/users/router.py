from fastapi import APIRouter, Depends, HTTPException, status

from src.users.dependencies import get_user_service
from src.users.exceptions import UserAlreadyExistsError
from src.users.schemas import CreateUserInput, CreateUserOutput
from src.users.service import UserService

users_router = APIRouter()


@users_router.post("")
async def create_user(
    create_user_payload: CreateUserInput,
    service: UserService = Depends(get_user_service),
) -> CreateUserOutput:
    try:
        return await service.create(create_user_payload)

    except UserAlreadyExistsError as exc:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email is already in use",
        ) from exc
