from fastapi import status

from src.auth.security import hash_password
from tests.factories import make_user

AUTH_LOGIN_URL = "/auth/login"


async def test_auth_login__missing_required_field(client):
    response = await client.post(
        AUTH_LOGIN_URL,
        json={"email": "email"},
    )

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_CONTENT
    assert response.json() == {
        "detail": [
            {
                "type": "missing",
                "loc": ["body", "password"],
                "msg": "Field required",
                "input": {"email": "email"},
            }
        ]
    }


async def test_auth_login__when_missing_user(db_session, client):
    password = "test_password"
    await make_user(
        db_session,
        hashed_password=hash_password(password),
    )

    response = await client.post(
        AUTH_LOGIN_URL,
        json={
            "email": "fake_email@fake.com",
            "password": password,
        },
    )

    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json() == {"detail": "Invalid email ou password"}


async def test_auth_login__when_invalid_password(db_session, client):
    user = await make_user(db_session)

    response = await client.post(
        AUTH_LOGIN_URL,
        json={
            "email": user.email,
            "password": "password",
        },
    )

    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json() == {"detail": "Invalid email ou password"}


async def test_auth_login__success(db_session, client):
    password = "test_password"
    user = await make_user(
        db_session,
        hashed_password=hash_password(password),
    )

    response = await client.post(
        AUTH_LOGIN_URL,
        json={
            "email": user.email,
            "password": password,
        },
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json().keys() == {"access_token", "refresh_token", "token_type"}
