import os
from dotenv import load_dotenv

from py2neo import Graph

load_dotenv()
GDB_URI = os.getenv("GDB_URI")
GDB_USERNAME = os.getenv("GDB_USERNAME")
GDB_PASSWORD = os.getenv("GDB_PASSWORD")
graph = Graph(uri=GDB_URI,auth=(GDB_USERNAME,GDB_PASSWORD))
