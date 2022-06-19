from fastapi.testclient import TestClient
import pytest
from app.main import app
from app import schemas

@pytest.fixture
def client():
    return TestClient(app)

def test_search_history(client):
    response = client.post("/analytics/search/history", json={"search":"FastAPI"})
    result = response.json()
    print(result)
    
def test_presence(client):
    response = client.post("/analytics/presence", json={"page":"FastAPI"})
    result = response.json()
    print(result)

def test_lesson(client):
    response = client.post("/analytics/lesson/34", json={"uuid":"34"})
    result = response.json()
    print(result)

def test_video(client):
    response = client.post("/analytics/video/34", json={"uuid":"34"})
    result = response.json()
    print(result)