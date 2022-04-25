from fastapi import APIRouter
import schemas

router = APIRouter(
    prefix = "/dashboard/expert",
    tags = ["Expert's dashboard"]
)

@router.get("/trainings/get/")
def get_trainings():
    ...

@router.post("/training/create")
def create_trainings(training: schemas.TrainingCreate):
    return training

@router.post("/training/chapter/create/")
def create_chapter(chapter: schemas.ChapterCreate):
    return chapter

@router.post("/training/chapter/lesson/create/")
def create_lesson(lesson: schemas.LessonCreate):
    return lesson

@router.put("/training/")
def update_trainings(training: schemas.TrainingUpdate):
    return training

@router.put("/training/chapter/")
def update_chapter(chapter: schemas.ChapterUpdate):
    return chapter

@router.put("/training/chapter/lesson/")
def update_lesson(lesson: schemas.LessonUpdate):
    return lesson

@router.delete("/training/delete/{training_id}")
def delete_trainings(training_id: int):
    ...

@router.delete("/training/chapter/delete/{chapter_id}")
def delete_chapter(chapter_id: int):
    ...

@router.delete("/training/chapter/lesson/delete/{lesson_id}")
def delete_lesson(lesson_id: int):
    ...
