from fastapi.testclient import TestClient
import pytest
from app.main import app
from app import schemas

@pytest.fixture
def client():
    return TestClient(app)

#def test_get_profile_with_login(client):
#    response = client.get("/profile/{login}")
#    profile = schemas.ProfileResponse(**response.json())
#    print(response.status_code)
#    print(profile)
    
#def test_get_profile(client):
#    response = client.get("/profile")
#    profile = schemas.ProfileResponse(**response.json())
#    print(response.status_code)
#    print(profile)
    
#def test_modify_login(client):
#    response = client.put("/profile/login")
#    print(response.status_code)

