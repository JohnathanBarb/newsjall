from fastapi import APIRouter, Depends, HTTPException, status

from src.auth.dependencies import get_auth_service
from src.auth.exceptions import InvalidCredentialsError
from src.auth.schemas import LoginRequestInput, TokenPairOutput
from src.auth.service import AuthService

auth_router = APIRouter()


@auth_router.post("/login")
async def login(
    payload: LoginRequestInput,
    auth_service: AuthService = Depends(get_auth_service),
) -> TokenPairOutput:
    try:
        return await auth_service.authenticate(
            email=payload.email,
            password=payload.password,
        )
    except InvalidCredentialsError as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email ou password",
        ) from exc
