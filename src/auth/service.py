from datetime import timedelta

from src.auth.exceptions import InvalidCredentialsException
from src.auth.schemas import TokenPairOutput
from src.auth.security import create_token, verify_password
from src.core.config import settings
from src.users.service import UserService


class AuthService:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    async def authenticate(self, email: str, password: str) -> TokenPairOutput:
        user = await self.user_service.get_with_credentials(email)
        if not user or not verify_password(
            raw_password=password,
            hashed_password=user.hashed_password,
        ):
            raise InvalidCredentialsException()

        return TokenPairOutput(
            access_token=create_token(
                subject=str(user.id),
                token_type="access",
                ttl=timedelta(minutes=settings.jwt_access_token_ttl_minutes),
                extra_claims={},
            ),
            refresh_token=create_token(
                subject=str(user.id),
                token_type="refresh",
                ttl=timedelta(days=settings.jwt_refresh_token_ttl_days),
                extra_claims={},
            ),
            token_type="bearer",
        )
