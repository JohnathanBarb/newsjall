from fastapi import status


async def test_health_ok(client):
    response = await client.get("/api/health")

    assert response.json() == {"app": "OK"}
    assert response.status_code == status.HTTP_200_OK
