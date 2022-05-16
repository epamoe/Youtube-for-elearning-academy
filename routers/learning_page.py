from fastapi import APIRouter, Depends, HTTPException, status
from oauth2 import get_current_user
from py2neo_schemas.nodes import Lesson, Video
from globals import graph
import schemas
from typing import List
router = APIRouter(
    prefix = "/dashboard",
    tags = ["Learning page"]
)

@router.get("/lesson/get/{lesson_uuid}", response_model = List[schemas.Video])
def get_lesson(lesson_uuid: str, user_login = Depends(get_current_user)):

    lesson = Lesson.match(graph).where("_.uuid='"+lesson_uuid+"'").first()
    query = """
        MATCH (l:Lesson)
        CALL db.index.fulltext.queryNodes("video_matching", $title) YIELD node 
        WITH node limit 100
        RETURN node
    """
    params = {
        "title": lesson.title
    }
    response = graph.run(query,params)
    videos = [
        Video(
            video_id = res["video_id"],
            title = res["title"],
            viewCount = res["viewCount"],
            channel_name = res["channel_name"],
            published_at = res["published_at"],
            description = res["description"],
            # subtitles = ,
            thumbnail = res["thumbnail"],
        )
        for res in response.data()
    ]
    return videos
