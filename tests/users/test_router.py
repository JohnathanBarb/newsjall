CREATE_USER_URL = "/api/users"


def test_create_user_bad_request(client):

    response = client.post(CREATE_USER_URL)
