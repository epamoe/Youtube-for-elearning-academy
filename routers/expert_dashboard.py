from fastapi import APIRouter, Depends, HTTPException, status
from functions import find_member
from oauth2 import get_current_user
from globals import graph 
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
    #Search for the user in the database. Returns the user if found, raise and exception otherwise
    member = find_member(user_login)

    new_training = Training(
        title=training.title,
        description=training.description,
        thumbnail=training.thumbnail
    )
    member.published_trainings.add(new_training)
    graph.push(member)

@router.post("/training/chapter/create/")
def create_chapter(chapter: schemas.ChapterCreate, user_login = Depends(get_current_user)):
    
    #Search for the user in the database. Returns the user if found, raise and exception otherwise
    member = find_member(user_login)

    training = Training.match(graph).where("_.uuid='"+chapter.training_uuid+"'").first()
    if not list(training.publisher)[0].login == member.login:
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
    
    #Search for the user in the database. Returns the user if found, raise and exception otherwise
    member = find_member(user_login)

    # Getting the chapter attached to the lesson and identified by chapter_id
    chapter = Chapter.match(graph).where("_.uuid = '"+lesson.chapter_uuid+"'").first()
    training = list(chapter.contained_by)[0]
    if not list(training.publisher)[0].login == member.login:
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
def update_trainings(training: schemas.TrainingUpdate, user_login = Depends(get_current_user)):
    #Search for the user in the database. Returns the user if found, raise and exception otherwise
    member = find_member(user_login)

    training_node = Training.match(graph).where("_.uuid = '"+training.uuid+"'").first()
    if not training_node:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail="This training doesn't exist"
        )
    
    if not list(training_node.publisher)[0].login == member.login:
        raise HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail="Only the trainings author can modify it"
        )

    training_node.title = training.title
    training_node.description = training.description
    training_node.thumbnail = training.thubmnail
    graph.push(training_node)

@router.put("/training/chapter/")
def update_chapter(chapter: schemas.ChapterUpdate, user_login = Depends(get_current_user)):
    #Search for the user in the database. Returns the user if found, raise and exception otherwise
    member = find_member(user_login)

    chapter_node = Chapter.match(graph).where("_.uuid = '"+chapter.uuid+"'").first()
    if not chapter_node:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail="This chapter doesn't exist"
        )
    containing_training = list(chapter_node.contained_by)[0]
    if not list(containing_training.publisher)[0].login == member.login:
        raise HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail="Only the trainings author can modify it"
        )
    chapter_node.title = chapter.title
    graph.push(chapter_node)

@router.put("/training/chapter/lesson/")
def update_lesson(lesson: schemas.LessonUpdate, user_login = Depends(get_current_user)):
    #Search for the user in the database. Returns the user if found, raise and exception otherwise
    member = find_member(user_login)

    lesson_node = Lesson.match(graph).where("_.uuid = '"+lesson.uuid+"'").first()
    if not lesson_node:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail="This lesson doesn't exist"
        )
    
    containing_chapter = list(lesson_node.subdivided)[0]
    containing_training = list(containing_chapter.contained_by)[0]
    if not list(containing_training.publisher)[0].login == member.login:
        raise HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail="Only the trainings author can modify it"
        )
    lesson_node.title = lesson.title
    # lesson_node.rank_nb = lesson.rank_nb
    graph.push(lesson_node)

@router.delete("/training/{uuid}")
def delete_trainings(uuid: str, user_login = Depends(get_current_user)):
    #Search for the user in the database. Returns the user if found, raise and exception otherwise
    member = find_member(user_login)

    training_node = Training.match(graph).where("_.uuid = '"+uuid+"'").first()
    if not training_node:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail="This training doesn't exist"
        )    
    if not list(training_node.publisher)[0].login == member.login:
        raise HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail="Only the training's author can delete it"
        )

    graph.run("MATCH (t:Training{uuid:'"+uuid+"'})-[r1:CONTAIN]->(c:Chapter)-[r2:SUBDIVIDE]->(l:Lesson) REMOVE c:Available, l:Available, t:Available")

@router.delete("/training/chapter/{uuid}")
def delete_chapter(uuid: str, user_login = Depends(get_current_user)):
    
    #Search for the user in the database. Returns the user if found, raise and exception otherwise
    member = find_member(user_login)

    chapter_node = Chapter.match(graph).where("_.uuid = '"+uuid+"'").first()
    if not chapter_node:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail="This chapter doesn't exist"
        )
    containing_training = list(chapter_node.contained_by)[0]
    if not list(containing_training.publisher)[0].login == member.login:
        raise HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail="Only the trainings author can modify it"
        )
    
    graph.run("MATCH (c:Chapter{uuid:'"+uuid+"'})-[r2:SUBDIVIDE]->(l:Lesson) REMOVE c:Available, l:Available")


@router.delete("/training/chapter/lesson/{uuid}")
def delete_lesson(uuid: str, user_login = Depends(get_current_user)):
    #Search for the user in the database. Returns the user if found, raise and exception otherwise
    member = find_member(user_login)

    lesson_node = Lesson.match(graph).where("_.uuid = '"+uuid+"'").first()
    if not lesson_node:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail="This lesson doesn't exist"
        )
    
    containing_chapter = list(lesson_node.subdivided)[0]
    containing_training = list(containing_chapter.contained_by)[0]
    if not list(containing_training.publisher)[0].login == member.login:
        raise HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail="Only the trainings author can modify it"
        )
    
    graph.run("MATCH (l:Lesson{uuid:'"+uuid+"'}) REMOVE l:Available")