from fastapi import APIRouter
import schemas
router = APIRouter(
    prefix = "/analytics",
    tags = ["Analytics"]
)

@router.post("/search/history")
def search(search: schemas.AnalyticsSearch):
    return search

@router.post("/presence")
def presence(page: schemas.AnalyticsPresence):
    return page


@router.get("/lesson/{id}")
def analytic_lesson(id):
    ...

@router.get("/video/{id}")
def analytic_video(id):
    ...
    