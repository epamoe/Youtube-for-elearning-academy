from fastapi.testclient import TestClient
import pytest
from app.main import app
from app import schemas

@pytest.fixture
def client():
    return TestClient(app)

def test_get_profile(client):
    response = client.get("/dashboard/profile")
    result = response.json()
    #if result.get("detail") == "This user doesn't exist":
    #    assert response.status_code == 404
    
    #else:
    #    assert response.status_code == 200
    
def test_modify_login(client):
    response = client.put("/dashboard/profile/login", json={"login":"G2"})
    result = response.json()
    print(response.status_code)

def test_modify_email(client):
    response = client.put("/dashboard/profile/email", json={"email":"ttappg14@gmail.com"})
    result = response.json()
    print(response.status_code)
    
def test_modify_email_confirm(client):
    response = client.get("/dashboard/profile/email/confirm/RECD2Yae", json={"confirmation_code":"RECD2Yae"})
    result = response.json()

def test_modify_password(client):
    response = client.get("/dashboard/profile/password", json={"current_password":"devops","password":"dev", "confirm_password":"dev"})
    result = response.json()
    print(result)

def test_notifications(client):
    response = client.get("/dashboard/notifications/")
    result = response.json()
    print(result)

def test_trainings(client):
    response = client.get("/dashboard/profile/trainings/")
    result = response.json()
    print(result)

def test_follow_training(client):
    response = client.get("/dashboard/user/training/follow/Ert56")
    print(response)

def test_expert_apply(client):
    response = client.get("/dashboard/expert/apply")
    print(response)