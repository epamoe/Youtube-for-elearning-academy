from fastapi.testclient import TestClient
import pytest
from app.main import app
from app import schemas

@pytest.fixture
def client():
    return TestClient(app)

def test_search(client):
    response = client.get("/landing/search/FastAPI for beginners", json={"query":"FastAPI for beginners"})
    result = response.json()
    print(result)

def test_filtered_search(client):
    response = client.get("/landing/search/filter/FastAPI", json={"query":"FastAPI"})
    result = response.json()
    print(result)

def test_get_domains(client):
    response = client.get("/landing/domains/get")
    result = response.json()
    print(result)

def test_search_on_dashboard(client):
    response = client.get("/dashboard/search/fhy68")
    result = response.json()
    print(result)
    
def test_get_training(client):
    response = client.get("/dashboard/training/get/fhy68")
    result = response.json()
    print(result)

def test_get_training_like(client):
    response = client.get("/dashboard/training/like/fhy68")
    result = response.json()
    print(result)
    
def test_get_training_star(client):
    response = client.get("/dashboard/training/review/star/fhy68")
    result = response.json()
    print(result)
    
def test_get_training_text(client):
    response = client.get("/dashboard/training/review/text/fhy68")
    result = response.json()
    print(result)