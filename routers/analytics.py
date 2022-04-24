from fastapi import APIRouter
import schemas
router = APIRouter(
    prefix = "/landing/analytics",
    tags = ["Analytics"]
)

@router.post("/search/history")
def search(search: schemas.AnalyticsSearch):
    return search

@router.post("/presence")
def presence(page: schemas.AnalyticsPresence):
    return page