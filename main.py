from accounts import token
from fastapi import FastAPI, Depends, status, Request
from fastapi.security import OAuth2PasswordRequestForm
from starlette.responses import  RedirectResponse
from accounts.api_classes.login_form import LoginForm
from accounts.data_classes.user import User
from accounts.registration_module.login_handler import LoginHandler
from accounts.oauth2 import get_current_user
import accounts.router as accounts_router
# from .accounts import router
import test_module.router as test_router


app = FastAPI() 
app.include_router(accounts_router.router)
app.include_router(test_router.router)


@app.get("/test")
def index(current_user: User = Depends(get_current_user)):
    return {
        "data" : "Hello World"
    }
    
@app.get("/test2")
def index(request: Request):
    client_host = request.url.netloc
    return {
        "client_host" : client_host
    }

import os
from dotenv import load_dotenv
from neo4j import GraphDatabase
load_dotenv()
uri = os.getenv("GDB_URI")
user = os.getenv("GDB_USERNAME")
password = os.getenv("GDB_PASSWORD")
driver = GraphDatabase.driver(uri=uri,auth=(user,password))
session = driver.session()

@app.get("/test3")
def index():
    return session.run("CREATE (n:Person{name:'uriel'}) return n").single()
    ...
    
@app.get("/redirect")
async def redirect():
    response = RedirectResponse(url='/redirected')
    return response


# There are two databases for the users login
# - A permanent database for the users whom are recognized as members of the site. They are the users whom have activated
# their account
# - A temporary database for the users whom have sent their datas, but haven't yet activated it