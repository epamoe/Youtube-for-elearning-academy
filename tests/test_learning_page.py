from fastapi.testclient import TestClient
import pytest
from app.main import app
from app import schemas

@pytest.fixture
def client():
    return TestClient(app)

def test_get_lesson(client):
    response = client.get("/dashboard/lesson/get/t545")
    result = response.json()
    print(result)