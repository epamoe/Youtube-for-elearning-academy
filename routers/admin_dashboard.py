from typing import List
from fastapi import APIRouter, Depends, HTTPException,status
from py2neo_schemas.nodes import User, Application
from schemas import ApplicationResponse

from oauth2 import get_current_user
from db_graph import graph

router = APIRouter(
    prefix = "/dashboard/admin",
    tags = ["Admin's dashboard"]
)

@router.get("/validate/{application_id}", status_code=status.HTTP_200_OK)
def validate(application_id: int, user_login = Depends(get_current_user)):
    user = User.match(graph,user_login).first()
    if not user.admin:
        raise HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail="You need admin rights to realize that operation"
        )

    application = Application.match(graph, application_id).first()
    if not application:
        raise HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail="This application doesn't exist"
        )

    if application.status == Application.PENDING:
        related_user = list(application.candidates)[0]
        related_user.member = True 
        graph.push(related_user)
        
    else:
        raise HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail="This application is already treated"
        )

@router.get("/member_application/", response_model=List[ApplicationResponse])
def get_applications(user_login = Depends(get_current_user)):
    user = User.match(graph,user_login).first()
    if not user.admin:
        raise HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail="You need admin rights to realize that operation"
        )

    applications =  list(Application.match(graph).where("_.status = '" + Application.PENDING + "'"))
    apps_users = [Application(status = app.status, user_login = list(app.candidates)[0].login) for app in applications]
    return apps_users
    ...