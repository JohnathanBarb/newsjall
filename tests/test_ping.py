from http import HTTPStatus


def test_ping_pong_request(client):
    response = client.get("/ping")

    assert response.json() == {"message": "pong"}
    assert response.status_code == HTTPStatus.OK
