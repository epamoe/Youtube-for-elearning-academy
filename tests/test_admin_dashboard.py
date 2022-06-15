from fastapi.testclient import TestClient
import pytest
from app.main import app
from app import schemas

@pytest.fixture
def client():
    return TestClient(app)

def test_validate_apply(client):
    response = client.get("/dashboard/admin/validate/df56ffd")
    result = response.json()
    print(result)
    
def test_applications(client):
    response = client.get("/dashboard/admin/member_application/")
    result = response.json()
    print(result)

