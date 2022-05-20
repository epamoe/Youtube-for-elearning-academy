from fastapi import APIRouter, Depends, HTTPException, status
from oauth2 import get_current_user
from py2neo_schemas.nodes import Lesson, Video
from globals import main_graph, video_graph
import schemas
from typing import List
router = APIRouter(
    prefix = "/dashboard",
    tags = ["Learning page"]
)

@router.get("/lesson/get/{lesson_uuid}", response_model = List[schemas.Video])
def get_lesson(lesson_uuid: str, user_login = Depends(get_current_user)):

    lesson = Lesson.match(main_graph).where("_.uuid='"+lesson_uuid+"'").first()
    # print(lesson.__node__)98bd82df-ce19-472c-bf00-c38c5205ebd8
    query = """
        MATCH (l:Lesson)
        CALL db.index.fulltext.queryNodes("video_matching", $title) YIELD node 
        WITH node limit 100
        RETURN node
    """
    params = {
        "title": lesson.title
    }
    response = video_graph.run(query,params)
    videos = [
        Video(
            video_id = res["node"]["video_id"],
            title = res["node"]["title"],
            viewCount = res["node"]["viewCount"],
            channel_name = res["node"]["channel_name"],
            published_at = res["node"]["published_at"],
            description = res["node"]["description"],
            # subtitles = ,
            thumbnail = res["node"]["thumbnail"],
        )
        for res in response.data()
    ]
    return videos
