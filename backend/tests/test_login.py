def test_login_returns_access_token(client):
    client.post(
        "/auth/register",
        json={"email": "login@example.com", "password": "secret123", "role": "customer"},
    )

    response = client.post(
        "/auth/login", json={"email": "login@example.com", "password": "secret123"}
    )

    assert response.status_code == 200
    body = response.json()
    assert body["token_type"] == "bearer"
    assert isinstance(body["access_token"], str) and body["access_token"]


def test_login_wrong_password_rejected(client):
    client.post(
        "/auth/register",
        json={"email": "login2@example.com", "password": "secret123", "role": "customer"},
    )

    response = client.post(
        "/auth/login", json={"email": "login2@example.com", "password": "wrongpass"}
    )

    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid email or password"


def test_login_unknown_email_rejected(client):
    response = client.post(
        "/auth/login", json={"email": "ghost@example.com", "password": "whatever"}
    )

    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid email or password"
