from fastapi import APIRouter, Depends, HTTPException, status
from oauth2 import get_current_user
from db_graph import graph 
from py2neo_schemas.nodes import User, Training, Chapter, Lesson
import schemas

router = APIRouter(
    prefix = "/dashboard/expert",
    tags = ["Expert's dashboard"]
)

@router.get("/trainings/get/")
def get_trainings():
    ...

@router.post("/training/create")
def create_trainings(training: schemas.TrainingCreate, user_login = Depends(get_current_user)):
    user = User.match(graph,user_login).first()
    if not user.member:
        raise HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail="You need member rights to realize that operation"
        )
    new_training = Training(
        title=training.title,
        description=training.description,
        thumbnail=training.thumbnail
    )
    user.published_trainings.add(new_training)
    graph.push(user)

@router.post("/training/chapter/create/")
def create_chapter(chapter: schemas.ChapterCreate, user_login = Depends(get_current_user)):
    user = User.match(graph,user_login).first()
    if not user.member :
        raise HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail="You need member rights to realize that operation"
        )
    training = Training.match(graph, chapter.training_id).first()
    if not list(training.publisher)[0].login == user.login:
        raise HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail="Only the training's author can modify it"
        )
    new_chapter = Chapter(
        title=chapter.title,
        rank_nb=chapter.rank_nb
    )
    training.chapters.add(new_chapter)
    graph.push(training)

@router.post("/training/chapter/lesson/create/")
def create_lesson(lesson: schemas.LessonCreate, user_login = Depends(get_current_user)):
    # Verifying user right to modify the training
    user = User.match(graph,user_login).first()
    if not user.member :
        raise HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail="You need member rights to realize that operation"
        )
    # Getting the chapter attached to the lesson and identified by chapter_id
    chapter = Chapter.match(graph, lesson.chapter_id).first()
    training = list(chapter.contained_by)[0]
    if not list(training.publisher)[0].login == user.login:
        raise HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail="Only the training's author can modify it"
        )
    
    # Creating the new lesson and adding it to the graph
    new_lesson = Lesson(
        title=lesson.title,
        rank_nb=lesson.rank_nb
    )
    chapter.subdivide.add(new_lesson)
    graph.push(chapter)
    ...

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
