from src.users.repository import UserRepository
from src.users.schemas import CreateUserInput, CreateUserOutput


class UserService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    async def create(self, user_create_payload: CreateUserInput) -> CreateUserOutput:
        # TODO: verify email is not duplicated

        # TODO: hash password

        hash_password = user_create_payload.password

        user = await self.repo.create(
            email=user_create_payload.email,
            hash_password=hash_password,
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
