from fastapi import APIRouter

router = APIRouter(
    prefix = "/dashboard",
    tags = ["Learning page"]
)

@router.get("/lesson/get/{lesson_id}")
def get_lesson(lesson_id: int):
    ...
