from http import HTTPStatus


async def test_health_ok(client):
    response = await client.get("/api/health")

    assert response.json() == {"app": "OK"}
    assert response.status_code == HTTPStatus.OK
