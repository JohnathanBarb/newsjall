from src.auth.security import hash_password
from src.users.exceptions import UserAlreadyExistsException
from src.users.repository import UserRepository
from src.users.schemas import CreateUserInput, CreateUserOutput


class UserService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    async def create(self, user_create_payload: CreateUserInput) -> CreateUserOutput:
        if await self.repo.get_by_email(user_create_payload.email):
            raise UserAlreadyExistsException()

        # TODO: hash password

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
