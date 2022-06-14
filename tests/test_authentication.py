from fastapi.testclient import TestClient
import pytest
from app.main import app
from app import schemas

@pytest.fixture
def client():
    return TestClient(app)

def test_register(client):
    response = client.post("/register", json={"login":"G3","email":"tapg14@gmail.com","password":"devps", "confirm_password":"devops"})
    result = response.json()
    if result.get("detail") == "The user already exists" or result.get("detail") == "Invalid or not existing email":
        print(result.get("detail"))
        assert response.status_code == 401
    
    elif result.get("detail") == "The password and the confirmation password don't match":
        print(result.get("detail"))
        assert response.status_code == 417
    
    elif result == None:
        print(result)
        assert response.status_code == 201


def test_login(client):
    response = client.post("/login",data={"username":"G2", "password":"devops"})
    result = response.json()
    if result.get("detail") == "The user doesn't exists":
        print(result.get("detail"))
        assert response.status_code == 404
    
    if result.get("detail") == "This user account isn't yet activated. Look for the activation link in your mail box":
        print(result.get("detail"))
        assert response.status_code == 401
    
    elif isinstance(result.get("access_token"), str):
        print(result.get("access_token"))
        assert response.status_code == 200
        
def test_activate(client):
    response = client.get("/activate/ZzI=")
    result = response.json()
    
    if result.get("detail") == "Invalid activation link":
        print(result.get("detail"))
        assert response.status_code == 401
    
    elif result.get("detail") == "Activation succeeded":
        print(result.get("detail"))
        assert response.status_code == 200