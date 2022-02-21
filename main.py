from accounts import token
from fastapi import FastAPI, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from starlette.responses import  RedirectResponse
from accounts.api_classes.login_form import LoginForm
from accounts.data_classes.user import User
from accounts.login.login_handler import LoginHandler
from accounts.oauth2 import get_current_user
import accounts.router as accounts_router

app = FastAPI() 
app.include_router(accounts_router.router)


@app.get("/test")
def index(current_user: User = Depends(get_current_user)):
    return {
        "data" : "Hello World"
    }
    
@app.get("/redirect")
async def redirect():
    response = RedirectResponse(url='/redirected')
    return response


# There are two databases for the users login
# - A permanent database for the users whom are recognized as members of the site. They are the users whom have activated
# their account
# - A temporary database for the users whom have sent their datas, but haven't yet activated it