from fastapi import APIRouter, Depends
from app.oauth2 import get_current_user
from py2neo_schemas.nodes import SearchInput, User
from app.globals import main_graph
router = APIRouter(
    prefix = "/analytics",
    tags = ["Analytics"]
)

@router.post("/search/history")
def search(search: str, user_login = Depends(get_current_user)):
    user = User.match(main_graph, user_login).first()
    search_input = SearchInput(content= search)
    user.search.add(search_input)
    main_graph.push(user)

@router.post("/presence")
def presence(page: str, user_login = Depends(get_current_user)):
    query = """
        MATCH (u:User{login:$user_login}) 
        MERGE (u)-[v:VISIT]->(p:Page{page:$page}) 
        ON CREATE SET v.nbr = 1 ON MATCH SET v.nbr = v.nbr + 1 """
    params = {
        "user_login" : user_login, 
        "page": page
    }
    main_graph.run(query, params)


@router.get("/lesson/{uuid}")
def analytic_lesson(uuid:int ,user_login = Depends(get_current_user)):
    query = """
        MATCH (u:User{login:$user_login}),(l:Lesson{uuid:$uuid}) 
        MERGE (u)-[c:WATCH]->(l) 
        ON CREATE SET c.nbr = 1 ON MATCH SET c.nbr = c.nbr + 1 
    """
    params = {
        "user_login" : user_login,
        "uuid" : uuid
    }
    main_graph.run(query, params)


# @router.get("/video/{video_id}")
# def analytic_video(video_id:str ,user_login = Depends(get_current_user)):
#     query = """
#         MATCH (u:User{login:$user_login}),(v:Video{video_id:$video_id}) 
#         MERGE (u)-[c:WATCH]->(v) 
#         ON CREATE SET c.nbr = 1 
#         ON MATCH SET c.nbr = c.nbr + 1 "
#     """
#     params = {
#         "user_login" : user_login,
#         "video_id" : video_id
#     }
#     main_graph.run(query, params)
#     ...
    