from pwdlib import PasswordHash
from pwdlib.hashers.argon2 import Argon2Hasher

_password_hash = PasswordHash((Argon2Hasher(),))


def hash_password(raw_password: str) -> str:
    return _password_hash.hash(raw_password)


def verify_password(raw_password: str, hashed_password: str) -> bool:
    return _password_hash.verify(raw_password, hashed_password)


def verify_and_update_password(raw_password: str, hashed_password: str):
    return _password_hash.verify_and_update(raw_password, hashed_password)
