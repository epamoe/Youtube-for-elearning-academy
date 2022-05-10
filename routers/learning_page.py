from fastapi import APIRouter, Depends, HTTPException, status
from oauth2 import get_current_user
from py2neo_schemas.nodes import Lesson, User
from globals import graph
import schemas
from typing import List
router = APIRouter(
    prefix = "/dashboard",
    tags = ["Learning page"]
)

@router.get("/lesson/get/{lesson_uuid}", response_model = List[schemas.Video])
def get_lesson(lesson_uuid: str, user_login = Depends(get_current_user)):
    user = User.match(graph,user_login).first()
    if not user :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="This user doesn't exist"
        )
    lesson = Lesson.match(graph).where("_.uuid='"+lesson_uuid+"'").first()
    videos = list(lesson.gather)
    return videos
