import os
from dotenv import load_dotenv
from fastapi import HTTPException,status

from py2neo import Graph

load_dotenv()
APP_NAME = os.getenv("APP_NAME")
GDB_URI = os.getenv("GDB_URI")
GDB_USERNAME = os.getenv("GDB_USERNAME")
GDB_PASSWORD = os.getenv("GDB_PASSWORD")

try:
    graph = Graph(uri=GDB_URI,auth=(GDB_USERNAME,GDB_PASSWORD))
except Exception:
    raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail="The connection to the database failed"
    )

encodeing='utf8'
