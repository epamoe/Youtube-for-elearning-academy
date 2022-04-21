from fastapi import APIRouter
import schemas
from typing import List

router = APIRouter(
    prefix = "/ydev",
    tags = ["Landing page search"]
)

@router.get("/landing/search/{query}", response_model = List[schemas.SearchResponse])
def search(query: str):
    return {"data": "response"}

@router.get("/landing/search/filter/{query}", response_model = List[str])
def filtered_search(query: str):
    return {"data": "response"}

@router.get("/landing/domains/get", response_model = List[str])
def get_domains():
    return {"data": "response"}

@router.get("/dashboard/search/{id}", response_model = List[schemas.SearchResponse])
def search_on_dashboard(id: int):
    ...

@router.get("/dashboard/training/get/{id}", response_model = schemas.TrainingResponse)
def get_training(id: int):
    ...

@router.get("/dashboard/training/like/{id}")
def training_like(id: int):
    ...

@router.get("/dashboard/training/review/star/{id}")
def training_star(id: int):
    ...

@router.get("/dashboard/training/review/text/{id}")
def training_text(id: int):
    ...