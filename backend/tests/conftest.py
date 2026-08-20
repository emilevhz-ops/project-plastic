import pytest
from fastapi.testclient import TestClient

from api.routes.auth import users_db
from main import app


@pytest.fixture(autouse=True)
def clear_users_db():
    users_db.clear()
    yield
    users_db.clear()


@pytest.fixture
def client():
    return TestClient(app)
