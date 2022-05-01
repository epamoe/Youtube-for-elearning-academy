from fastapi import APIRouter

router = APIRouter(
    prefix = "/dashboard",
    tags = ["Learning page"]
)

@router.get("/lesson/get/{lesson_uuid}")
def get_lesson(lesson_uuid: int):
    ...
