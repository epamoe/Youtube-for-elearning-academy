from fastapi import APIRouter, Depends, HTTPException, status
from app.functions import find_member
from app.oauth2 import get_current_user
from app.globals import main_graph 
from py2neo_schemas.nodes import User, Training, Chapter, Lesson
from app import schemas
from typing import List

router = APIRouter(
    prefix = "/dashboard/expert",
    tags = ["Expert's dashboard"]
)

@router.get("/trainings/{login}", response_model = List[schemas.Training])
def get_trainings(login:str):
    member = find_member(login)
    trainings = [schemas.Training(
        uuid = t.__node__.identity,
        title = t.title,
        description = t.description,
        students_number = t.students_number,
        mark = t.mark,
        thumbnail = t.thumbnail,
        author_login = list(t.publisher)[0].login
    ) for t in list(member.published_trainings)]
    return trainings
    ...

@router.post("/training/create", response_model=schemas.CreationResponse)
def create_trainings(training: schemas.TrainingCreate, user_login = Depends(get_current_user)):
    #Search for the user in the database. Returns the user if found, raise and exception otherwise
    find_member(user_login)
    query = """
        MATCH (m:Member{login:$login})
        MERGE (m)-[:PUBLISH]-(t:Available:Training{title:$title, description: $description, thumbnail: $thumbnail, students_number: 0, mark: 0})
        SET t.uuid = ID(t)
        RETURN ID(t) as uuid
    """
    params = {
        "login": user_login,
        "title": training.title,
        "description": training.description,
        "thumbnail": training.thumbnail
    }

    response = main_graph.run(query, params)
    return schemas.CreationResponse(uuid=response.data()[0]["uuid"])

@router.post("/training/chapter/create/")
def create_chapter(chapter: schemas.ChapterCreate, user_login = Depends(get_current_user)):
    
    #Search for the user in the database. Returns the user if found, raise and exception otherwise
    find_member(user_login)

    query = """
        MATCH (t:Training{uuid:$training_uuid})
        MERGE (t)-[:CONTAIN]-(c:Available:Chapter{title:$title, rank_nb: $rank_nb})
        SET c.uuid = ID(c)
        RETURN ID(c) as uuid
    """
    params = {
        "training_uuid": chapter.training_uuid,
        "title": chapter.title,
        "rank_nb": chapter.rank_nb
    }
    
    response = main_graph.run(query, params)
    return schemas.CreationResponse(uuid=response.data()[0]["uuid"])

@router.post("/training/chapter/lesson/create/")
def create_lesson(lesson: schemas.LessonCreate, user_login = Depends(get_current_user)):
    
    #Search for the user in the database. Returns the user if found, raise and exception otherwise
    find_member(user_login)

    query = """
        MATCH (t:Chapter{uuid:$chapter_uuid})
        MERGE (t)-[:CONTAIN]-(c:Available:Lesson{title:$title, rank_nb: $rank_nb})
        SET c.uuid = ID(c)
        RETURN ID(c) as uuid
    """
    params = {
        "chapter_uuid": lesson.chapter_uuid,
        "title": lesson.title,
        "rank_nb": lesson.rank_nb
    }
    
    response = main_graph.run(query, params)
    return schemas.CreationResponse(uuid=response.data()[0]["uuid"])
  

@router.put("/training/")
def update_trainings(training: schemas.TrainingUpdate, user_login = Depends(get_current_user)):
    #Search for the user in the database. Returns the user if found, raise and exception otherwise
    member = find_member(user_login)

    training_node = Training.match(main_graph,training.training_uuid).first()
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
    main_graph.push(training_node)

@router.put("/training/chapter/")
def update_chapter(chapter: schemas.ChapterUpdate, user_login = Depends(get_current_user)):
    #Search for the user in the database. Returns the user if found, raise and exception otherwise
    member = find_member(user_login)

    chapter_node = Chapter.match(main_graph,chapter.chapter_uuid).first()
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
    chapter_node.uuid = chapter_node.__node__.identity
    chapter_node.title = chapter.title
    main_graph.push(chapter_node)

@router.put("/training/chapter/lesson/")
def update_lesson(lesson: schemas.LessonUpdate, user_login = Depends(get_current_user)):
    #Search for the user in the database. Returns the user if found, raise and exception otherwise
    member = find_member(user_login)

    lesson_node = Lesson.match(main_graph,lesson.lesson_uuid).first()
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
    lesson_node.uuid = lesson_node.__node__.identity
    # lesson_node.rank_nb = lesson.rank_nb
    main_graph.push(lesson_node)

@router.delete("/training/{uuid}")
def delete_trainings(uuid: int, user_login = Depends(get_current_user)):
    #Search for the user in the database. Returns the user if found, raise and exception otherwise
    member = find_member(user_login)

    training_node = Training.match(main_graph,uuid).first()
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
    query="""
        MATCH (t:Training{uuid:$uuid})-[r1:CONTAIN]->(c:Chapter)-[r2:SUBDIVIDE]->(l:Lesson) REMOVE c:Available, l:Available, t:Available
    """
    params = {
        "uuid": uuid
    }
    main_graph.run(query, params)

@router.delete("/training/chapter/{uuid}")
def delete_chapter(uuid: int, user_login = Depends(get_current_user)):
    
    #Search for the user in the database. Returns the user if found, raise and exception otherwise
    member = find_member(user_login)

    chapter_node = Chapter.match(main_graph,uuid).first()
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
    query = """
        MATCH (c:Chapter{uuid:$uuid})-[r2:SUBDIVIDE]->(l:Lesson) REMOVE c:Available, l:Available
    """
    params={
        "uuid":uuid
    }
    main_graph.run(query, params)


@router.delete("/training/chapter/lesson/{uuid}")
def delete_lesson(uuid: int, user_login = Depends(get_current_user)):
    #Search for the user in the database. Returns the user if found, raise and exception otherwise
    member = find_member(user_login)

    lesson_node = Lesson.match(main_graph,uuid).first()
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
    
    query = """
        MATCH (l:Lesson{uuid:$uuid}) REMOVE l:Available
    """
    params={
        "uuid":uuid
    }
    main_graph.run(query, params)
    # main_graph.run("MATCH (l:Lesson{uuid:'"+uuid+"'}) REMOVE l:Available")