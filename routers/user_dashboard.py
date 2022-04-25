from fastapi import APIRouter, Depends, HTTPException,status
from oauth2 import get_current_user
import schemas
from py2neo_schemas.nodes.user import User
from db_graph import graph

router = APIRouter(
    prefix = "/dashboard",
    tags = ["User's dashboard"]
)

@router.get("/profile")
def get_profile():
    ...

@router.get("/profile/{login}")
def get_profile():
    ...
    
@router.put("/profile/login")
def update_login(user_login: schemas.UserUpdateLogin):
    return user_login

@router.put("/profile/email")
def update_email(user_email: schemas.UserUpdateEmail):
    return user_email

@router.put("/profile/password")
def update_password(user_password: schemas.UserUpdatePassword):
    return user_password

@router.put("/profile/profile_image")
def update_profile_image(user_profile_image: schemas.UserUpdateProfileImage):
    return user_profile_image

@router.get("/profile/expert/{id}")
def get_expert_profile(id):
    ...

@router.get("/notifications/")
def get_notifications():
    ...
    
@router.get("/profile/trainings/")
def get_trainings():
    ...
    
@router.get("/user/training/follow/")
def follow_training():
    ...
    
@router.get("/expert/apply")
def apply(user_login = Depends(get_current_user)):
    user_node = User.match(graph, user_login).first()
    if user_node.did_apply():
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="This user already applied to become a member")
    user_node.apply()
    graph.push(user_node)
    