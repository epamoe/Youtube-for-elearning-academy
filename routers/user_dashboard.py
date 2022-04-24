from fastapi import APIRouter, Depends
from oauth2 import get_current_user
import schemas
from py2neo_schemas.nodes.user import User
from py2neo_schemas.nodes.application import Application
from py2neo import Graph

import os
from dotenv import load_dotenv
router = APIRouter(
    prefix = "/dashboard",
    tags = ["User's dashboard"]
)


load_dotenv()
GDB_URI = os.getenv("GDB_URI")
GDB_USERNAME = os.getenv("GDB_USERNAME")
GDB_PASSWORD = os.getenv("GDB_PASSWORD")
graph = Graph(uri=GDB_URI,auth=(GDB_USERNAME,GDB_PASSWORD))

@router.get("/profile/get")
def get_profile():
    ...
    
@router.put("/profile/update/login")
def update_login(user_login: schemas.UserUpdateLogin):
    return user_login

@router.put("/profile/update/email")
def update_email(user_email: schemas.UserUpdateEmail):
    return user_email

@router.put("/profile/update/password")
def update_password(user_password: schemas.UserUpdatePassword):
    return user_password

@router.put("/profile/update/profile_image")
def update_profile_image(user_profile_image: schemas.UserUpdateProfileImage):
    return user_profile_image

@router.get("/profile/expert/get/{id}")
def get_expert_profile(id):
    ...

@router.get("/analytics/lesson/{id}")
def analytic_lesson(id):
    ...

@router.get("/analytics/video/{id}")
def analytic_video(id):
    ...
    
@router.get("/notifications/get/")
def get_notifications():
    ...
    
@router.get("/user/trainings/get/")
def get_trainings():
    ...
    
@router.get("/user/training/follow/")
def follow_training():
    ...
    
@router.get("/expert/apply")
def apply(user_login = Depends(get_current_user)):
    user_node = User.match(graph, user_login).first()
    user_node.apply()
    graph.push(user_node)
    