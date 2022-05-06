from fastapi import APIRouter, Depends
from functions import find_member
from oauth2 import get_current_user
import schemas
from py2neo_schemas.nodes import Domain
from typing import List
from globals import graph
from py2neo_schemas.nodes import Training

router = APIRouter(
    tags = ["Landing page search"]
)

@router.get("/landing/search/{query}", response_model = List[schemas.Training])
def search(query: str):
    request = """
        CALL db.index.fulltext.queryNodes("training", $query) YIELD node
        MATCH (user)-[:PUBLISH]->(node)
        RETURN node, user.login as author_login
    """
    params = {
        "query" : query
    }
    response = graph.run(request, params)
    result = []
    
    result = [schemas.Training(
        title = t["node"]["title"],
        description= t["node"]["description"],
        mark = t["node"]["mark"],
        students_number=t["node"]["students_number"],
        thumbnail=t["node"]["thumbnail"],
        uuid = t["node"]["uuid"],
        author_login=t["author_login"]
    ) for t in response.data()]

    return result

@router.get("/landing/search/filter/{query}", response_model = List[str])
def filtered_search(query: str):
    return {"data": "response"}

@router.get("/landing/domains/get", response_model = List[str])
def get_domains(): 
    domains = list(Domain.match(graph))
    domains = [domain.content for domain in list(domains)]
    return domains

@router.get("/dashboard/search/{uuid}", response_model = List[schemas.Training])
def search_on_dashboard(uuid: str):
    training = Training.match(graph).where("_.uuid='"+uuid+"'").first()
    domain = list(training.domain)[0]
    trainings = list(domain.trainings)
    
    response = [ ]
    for t in trainings:
        if t.uuid != uuid:
            response.append(
                schemas.Training(
                    uuid = t.uuid,
                    title = t.title,
                    description = t.description,
                    students_number = t.students_number,
                    mark = t.mark,
                    thumbnail = t.thumbnail,
                    author_login = list(t.publisher)[0].login
                )
            )
    return response

@router.get("/dashboard/training/get/{uuid}", response_model = schemas.DashboardTraining)
def get_training(uuid: str):
    training_node = Training.match(graph).where("_.uuid = '"+uuid+"'").first()
    return schemas.DashboardTraining(
        uuid = training_node.uuid,
        title = training_node.title,
        description = training_node.description,
        students_number = training_node.students_number,
        mark = training_node.mark,
        thumbnail = training_node.thumbnail,
        author_login = list(training_node.publisher)[0].login,
        chapters = [
            schemas.Chapter(
                title = chapter.title,
                rank_nb = chapter.rank_nb,
                uuid = chapter.uuid, 
                lessons = list(chapter.subdivide)
            ) for chapter in list(training_node.chapters)
        ]
    )

    ...

@router.get("/dashboard/training/like/{uuid}")
def training_like(uuid: str, user_login = Depends(get_current_user)):
    member = find_member(user_login)
    training = Training.match(graph).where("_.uuid = '"+uuid+"'").first()
    member.like_training.add(training)
    graph.push(member)
    ...

@router.get("/dashboard/training/review/star/{uuid}")
def training_star(uuid: str, mark: int, user_login = Depends(get_current_user)):
    query = """
        MATCH (u:User{login:$user_login}),(t:Training{uuid:$uuid}) 
        MERGE (u)-[r:REVIEW_STAR]->(t)
        SET r.mark = $mark
    """
    params = {
        "user_login" : user_login,
        "uuid" : uuid,
        "mark" : mark
    }
    graph.run(query, params)

@router.get("/dashboard/training/review/text/{uuid}")
def training_text(uuid: str, content: str, user_login = Depends(get_current_user)):
    query = """
        MATCH (u:User{login:$user_login}),(t:Training{uuid:$uuid}) 
        MERGE (u)-[r:REVIEW_TEXT{content:$content}]->(t) 
    """
    params = {
        "user_login" : user_login,
        "uuid" : uuid,
        "content" : content
    }
    graph.run(query, params)