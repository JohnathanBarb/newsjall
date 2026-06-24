import uuid
from datetime import UTC, datetime, timedelta
from typing import Literal

import jwt
from pwdlib import PasswordHash
from pwdlib.hashers.argon2 import Argon2Hasher

from src.core.config import settings

TokenType = Literal["access", "refresh"]

_password_hash = PasswordHash((Argon2Hasher(),))


def hash_password(raw_password: str) -> str:
    return _password_hash.hash(raw_password)


def verify_password(raw_password: str, hashed_password: str) -> bool:
    return _password_hash.verify(raw_password, hashed_password)


def verify_and_update_password(
    raw_password: str, hashed_password: str
) -> tuple[bool, str | None]:
    return _password_hash.verify_and_update(raw_password, hashed_password)


def create_token(
    subject: str,
    token_type: TokenType,
    ttl: timedelta,
    extra_claims: dict[str, str] | None,
) -> str:
    now = datetime.now(UTC)
    payload = {
        "sub": subject,
        "iat": int(now.timestamp()),
        "exp": int((now + ttl).timestamp()),
        "iss": settings.jwt_issuer,
        "type": token_type,
        "jti": str(uuid.uuid4()),
    }
    if extra_claims:
        payload.update(extra_claims)
    return jwt.encode(
        payload,
        settings.jwt_secret,
        algorithm=settings.jwt_algorithm,
    )


def decode_token(token: str, expected_token_type: TokenType) -> dict[str, str]:
    payload = jwt.decode(
        token,
        settings.jwt_secret,
        algorithms=[settings.jwt_algorithm],
        issuer=settings.jwt_issuer,
        options={"require": ["exp", "iat", "sub", "type"]},
    )
    if payload.get("type") != expected_token_type:
        raise jwt.InvalidTokenError("Expected token type")

    return payload
