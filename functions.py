from py2neo_schemas.nodes import User
from fastapi import HTTPException, status
from db_graph import graph

def find_member(user_login):
    #Search for the user in the database. Returns the user if found, raise and exception otherwise
    user = User.match(graph,user_login).first()
    if not user.member:
        raise HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail="You are not a member"
        )
    return user