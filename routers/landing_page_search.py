from fastapi import APIRouter
import schemas
from py2neo_schemas.nodes import Domain
from typing import List
from db_graph import graph

router = APIRouter(
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
    domains = list(Domain.match(graph))
    domains = [domain.content for domain in list(domains)]
    return domains

@router.get("/dashboard/search/{id}", response_model = List[schemas.SearchResponse])
def search_on_dashboard(id: int):
    ...

@router.get("/dashboard/training/get/{uuid}", response_model = schemas.TrainingResponse)
def get_training(uuid: int):
    ...

@router.get("/dashboard/training/like/{uuid}")
def training_like(uuid: int):
    ...

@router.get("/dashboard/training/review/star/{uuid}")
def training_star(uuid: int, mark: int):
    ...

@router.get("/dashboard/training/review/text/{uuid}")
def training_text(uuid: int, content: str):
    ...