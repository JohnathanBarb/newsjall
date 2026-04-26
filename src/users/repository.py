from sqlalchemy.ext.asyncio import AsyncSession

from src.users.models import User


class UserRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(
        self,
        email: str,
        hash_password: str,
        name: str,
    ) -> User:
        user = User(email=email, hash_password=hash_password, name=name)
        self.db.add(user)
        await self.db.flush()
        return user
