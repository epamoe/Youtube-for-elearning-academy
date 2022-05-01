from fastapi import APIRouter, Depends
from oauth2 import get_current_user
from py2neo_schemas.nodes import SearchInput, User
from db_graph import graph
router = APIRouter(
    prefix = "/analytics",
    tags = ["Analytics"]
)

@router.post("/search/history")
def search(search: str, user_login = Depends(get_current_user)):
    user = User.match(graph, user_login).first()
    search_input = SearchInput(content= search)
    user.search.add(search_input)
    graph.push(user)

@router.post("/presence")
def presence(page: str, user_login = Depends(get_current_user)):
    graph.run("MATCH (u:User{login:'"+user_login+"'}) MERGE (u)-[v:VISIT]->(p:Page{content:'"+page+"'}) ON CREATE SET v.nbr = 1 ON MATCH SET v.nbr = v.nbr + 1 ")


@router.get("/lesson/{uuid}")
def analytic_lesson(uuid:str ,user_login = Depends(get_current_user)):
    graph.run("MATCH (u:User{login:'"+user_login+"'}),(l:Lesson{uuid:'"+str(uuid)+"'}) MERGE (u)-[c:WATCH]->(l) ON CREATE SET c.nbr = 1 ON MATCH SET c.nbr = c.nbr + 1 ")


@router.get("/video/{video_id}")
def analytic_video(uuid:str ,user_login = Depends(get_current_user)):
    graph.run("MATCH (u:User{login:'"+user_login+"'}),(v:Video{uuid:'"+str(uuid)+"'}) MERGE (u)-[c:WATCH]->(v) ON CREATE SET c.nbr = 1 ON MATCH SET c.nbr = c.nbr + 1 ")
    ...
    