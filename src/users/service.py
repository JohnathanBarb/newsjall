import uuid

from src.auth.security import hash_password
from src.users.exceptions import UserAlreadyExistsException
from src.users.models import User
from src.users.repository import UserRepository
from src.users.schemas import CreateUserInput, CreateUserOutput


class UserService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    async def get_by_id(self, id: uuid.UUID) -> CreateUserOutput | None:
        user = await self.repo.get_by_id(id=id)
        if not user:
            return None
        return CreateUserOutput(
            id=user.id,
            name=user.name,
            email=user.email,
            created_at=user.created_at,
            updated_at=user.updated_at,
        )

    async def get_with_credentials(self, email: str) -> User | None:
        return await self.repo.get_by_email(email=email)

    async def create(self, user_create_payload: CreateUserInput) -> CreateUserOutput:
        if await self.repo.get_by_email(user_create_payload.email):
            raise UserAlreadyExistsException()

        hashed_password = hash_password(user_create_payload.password)

        user = await self.repo.create(
            email=user_create_payload.email,
            hashed_password=hashed_password,
            name=user_create_payload.name,
        )

        await self.repo.db.commit()
        return CreateUserOutput(
            id=user.id,
            name=user.name,
            email=user.email,
            created_at=user.created_at,
            updated_at=user.updated_at,
        )
