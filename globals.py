import os
from dotenv import load_dotenv
from fastapi import HTTPException,status

from py2neo import Graph

load_dotenv()
APP_NAME = os.getenv("APP_NAME")

MAIN_GDB_URI = os.getenv("MAIN_GDB_URI")
MAIN_GDB_USERNAME = os.getenv("MAIN_GDB_USERNAME")
MAIN_GDB_PASSWORD = os.getenv("MAIN_GDB_PASSWORD")

VIDEO_GDB_URI = os.getenv("VIDEO_GDB_URI")
VIDEO_GDB_USERNAME = os.getenv("VIDEO_GDB_USERNAME")
VIDEO_GDB_PASSWORD = os.getenv("VIDEO_GDB_PASSWORD")

print(MAIN_GDB_URI)

try:
    main_graph = Graph(uri=MAIN_GDB_URI,auth=(MAIN_GDB_USERNAME,MAIN_GDB_PASSWORD))
except Exception:
    raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail="The connection to the main database failed"
    )

try:
    video_graph = Graph(uri=VIDEO_GDB_URI,auth=(VIDEO_GDB_USERNAME,VIDEO_GDB_PASSWORD))
except Exception:
    raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail="The connection to the videos database failed"
    )

encodeing='utf8'
