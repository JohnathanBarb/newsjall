from datetime import datetime
from http import HTTPStatus

from sqlalchemy import select

from src.users.models import User

CREATE_USER_URL = "/api/users"


async def test_create_user__without_full_body(client):

    response = await client.post(CREATE_USER_URL)

    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY


async def test_create_user__missing_required_field(client):

    response = await client.post(
        CREATE_USER_URL,
        json={"email": "email", "password": "password"},
    )

    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
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


async def test_create_user__success(db_session, client):

    response = await client.post(
        CREATE_USER_URL,
        json={"email": "email", "password": "password", "name": "name"},
    )

    assert response.status_code == HTTPStatus.OK

    result = await db_session.execute(select(User))
    user = result.scalars().one()

    response_json = response.json()

    assert response_json["id"] == str(user.id)
    assert response_json["name"] == user.name
    assert response_json["email"] == user.email
    assert datetime.fromisoformat(response_json["updated_at"]) == user.updated_at
    assert datetime.fromisoformat(response_json["created_at"]) == user.created_at
