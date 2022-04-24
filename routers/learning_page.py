from fastapi import APIRouter

router = APIRouter(
    prefix = "/dashboard"
)

@router.get("/lesson/get/{lesson_id}")
def get_lesson(lesson_id: int):
    ...
