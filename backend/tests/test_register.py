from api.routes.auth import users_db


def test_register_creates_user(client):
    response = client.post(
        "/auth/register",
        json={"email": "new@example.com", "password": "secret123", "role": "customer"},
    )

    assert response.status_code == 200
    assert response.json() == {"message": "User registered successfully"}


def test_register_duplicate_email_rejected(client):
    payload = {"email": "dup@example.com", "password": "secret123", "role": "customer"}
    client.post("/auth/register", json=payload)

    response = client.post("/auth/register", json=payload)

    assert response.status_code == 400
    assert response.json()["detail"] == "Email already registered"


def test_register_stores_hashed_password(client):
    client.post(
        "/auth/register",
        json={"email": "hash@example.com", "password": "secret123", "role": "admin"},
    )

    user = users_db["hash@example.com"]
    assert user.hashed_password != "secret123"
    assert user.role == "admin"
    assert user.is_active is True
