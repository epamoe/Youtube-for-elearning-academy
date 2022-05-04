from fastapi import APIRouter
import schemas
from typing import List
router = APIRouter(
    prefix = "/dashboard",
    tags = ["Learning page"]
)

@router.get("/lesson/get/{lesson_uuid}", response_model = List[schemas.Video])
def get_lesson(lesson_uuid: int):
    ...
