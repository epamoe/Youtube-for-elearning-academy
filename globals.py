import os
from dotenv import load_dotenv
from fastapi import HTTPException,status

from py2neo import Graph

load_dotenv()
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


def encode_password(password) -> str:
    from passlib.context import CryptContext    
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    hashed_password = pwd_context.hash(password)
    return hashed_password