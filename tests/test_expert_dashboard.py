from fastapi.testclient import TestClient
import pytest
from app.main import app
from app import schemas

@pytest.fixture
def client():
    return TestClient(app)

def test_trainings(client):
    response = client.get("/dashboard/expert/training/G2")
    result = response.json()
    print(result)

def test_create_training(client):
    response = client.post("/dashboard/expert/training/create", json={"title":"Django backend and React frontend","description":"Course about the creation of web apps...","thumbnail":"ABC"})
    result = response.json()
    print(result)
    
def test_create_chapter(client):
    response = client.post("/dashboard/expert/training/chapter/create", json={"training_uuid":20,"title":"Django backend and React frontend","rank_nb":20})
    result = response.json()
    print(result)
    
def test_create_lesson(client):
    response = client.post("/dashboard/expert/training/chapter/lesson/create", json={"chapter_uuid":2,"title":"Django backend and React frontend","rank_nb":20})
    result = response.json()
    print(result)
    
def test_update_training(client):
    response = client.post("/dashboard/expert/training/", json={"training_uuid":20,"title":"Django backend and React frontend","description":"Course about the creation of web apps...","thumbnail":"ABC"})
    result = response.json()
    print(result)
    
def test_update_chapter(client):
    response = client.post("/dashboard/expert/training/chapter/", json={"chapter_uuid":20,"title":"Django backend and React frontend","rank_nb":20})
    result = response.json()
    print(result)
    
def test_update_lesson(client):
    response = client.post("/dashboard/expert/training/chapter/lesson/", json={"lesson_uuid":2,"title":"Django backend and React frontend","rank_nb":20})
    result = response.json()
    print(result)

def test_delete_training(client):
    response = client.delete("/dashboard/expert/training/20", json={"uuid":20})
    result = response.json()
    print(result)
    
def test_delete_chapter(client):
    response = client.delete("/dashboard/expert/training/chapter/20", json={"uuid":20})
    result = response.json()
    print(result)
    
def test_delete_lesson(client):
    response = client.delete("/dashboard/expert/training/chapter/lesson/20", json={"uuid":20})
    result = response.json()
    print(result)