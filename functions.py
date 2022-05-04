from py2neo_schemas.nodes import User
from fastapi import HTTPException, status
from globals import graph

def find_member(user_login):
    #Search for the user in the database. Returns the user if found, raise and exception otherwise
    user = User.match(graph,user_login).first()
    if not user.member:
        raise HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail="You are not a member"
        )
    return user

def encode_password(password) -> str:
    from passlib.context import CryptContext    
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    hashed_password = pwd_context.hash(password)
    return hashed_password