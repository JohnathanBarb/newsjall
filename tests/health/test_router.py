from http import HTTPStatus


def test_health_ok(client):
    response = client.get("/api/health")

    assert response.json() == {"app": "OK"}
    assert response.status_code == HTTPStatus.OK
