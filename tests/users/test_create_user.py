from datetime import datetime

from fastapi import status
from sqlalchemy import select

from src.users.models import User
from tests.factories import make_user

CREATE_USER_URL = "/api/users"


async def test_create_user__without_full_body(client):

    response = await client.post(CREATE_USER_URL)

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_CONTENT


async def test_create_user__missing_required_field(client):

    response = await client.post(
        CREATE_USER_URL,
        json={"email": "email", "password": "password"},
    )

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_CONTENT
    assert response.json() == {
        "detail": [
            {
                "type": "missing",
                "loc": ["body", "name"],
                "msg": "Field required",
                "input": {"email": "email", "password": "password"},
            }
        ]
    }


async def test_create_user__with_email_existing(db_session, client):

    existing_user = await make_user(db_session)

    response = await client.post(
        CREATE_USER_URL,
        json={
            "email": existing_user.email,
            "password": "password",
            "name": "name",
        },
    )

    assert response.status_code == status.HTTP_409_CONFLICT
    assert response.json() == {"detail": "Email is already in use"}


async def test_create_user__success(db_session, client):

    response = await client.post(
        CREATE_USER_URL,
        json={"email": "email", "password": "password", "name": "name"},
    )

    assert response.status_code == status.HTTP_200_OK
    result = await db_session.execute(select(User))
    user = result.scalars().one()

    response_json = response.json()

    assert response_json["id"] == str(user.id)
    assert response_json["name"] == user.name
    assert response_json["email"] == user.email
    assert datetime.fromisoformat(response_json["updated_at"]) == user.updated_at
    assert datetime.fromisoformat(response_json["created_at"]) == user.created_at
