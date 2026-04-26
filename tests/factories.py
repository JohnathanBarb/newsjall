import uuid

from src.core.database import AsyncSession
from src.users.models import User


async def make_user(db_session: AsyncSession, **overrides) -> User:

    defaults = {
        "email": f"{uuid.uuid4()}@example.com",
        "name": "Test User",
        "hash_password": "blah",  # TODO: pass hashpassword when hashing password
    }

    user = User(**{**defaults, **overrides})
    db_session.add(user)
    await db_session.flush()

    return user
