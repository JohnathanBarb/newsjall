import uuid

from src.auth.security import hash_password
from src.core.database import AsyncSession
from src.users.models import User


async def make_user(db_session: AsyncSession, **overrides) -> User:

    defaults = {
        "email": f"{uuid.uuid4()}@example.com",
        "name": "Test User",
        "hashed_password": hash_password("blah"),
    }

    user = User(**{**defaults, **overrides})
    db_session.add(user)
    await db_session.flush()

    return user
