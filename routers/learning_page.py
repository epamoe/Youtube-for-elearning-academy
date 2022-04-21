from fastapi import APIRouter

router = APIRouter(
    prefix = "/ydev/dashboard"
)

@router.get("/lesson/get/{lesson_id}")
def get_lesson(lesson_id: int):
    ...
