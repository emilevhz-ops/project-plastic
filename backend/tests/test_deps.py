import pytest
from fastapi import HTTPException
from fastapi.security import HTTPAuthorizationCredentials

from api.deps import get_current_user
from api.routes.auth import users_db
from core.models import User
from core.security import create_access_token, hash_password


def _credentials(token: str) -> HTTPAuthorizationCredentials:
    return HTTPAuthorizationCredentials(scheme="Bearer", credentials=token)


def test_get_current_user_returns_user_for_valid_token():
    users_db["deps@example.com"] = User(
        id="1",
        email="deps@example.com",
        hashed_password=hash_password("secret123"),
        role="partner",
        is_active=True,
    )
    token = create_access_token(data={"sub": "deps@example.com", "role": "partner"})

    user = get_current_user(_credentials(token))

    assert user.email == "deps@example.com"
    assert user.role == "partner"


def test_get_current_user_rejects_invalid_token():
    with pytest.raises(HTTPException) as exc_info:
        get_current_user(_credentials("not-a-real-token"))

    assert exc_info.value.status_code == 401


def test_get_current_user_rejects_token_for_unknown_user():
    token = create_access_token(data={"sub": "ghost@example.com", "role": "customer"})

    with pytest.raises(HTTPException) as exc_info:
        get_current_user(_credentials(token))

    assert exc_info.value.status_code == 401
