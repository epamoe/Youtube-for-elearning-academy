from fastapi import FastAPI, status, Depends, Response, HTTPException
from starlette.responses import RedirectResponse
from accounts.api_classes.login_form import LoginForm
from accounts.api_classes.registration_form import RegistrationForm
from accounts.db_driver import DBDriver
from accounts.login.login_handler import LoginHandler
from accounts.registration.registration_handler import RegistrationHandler

# prefix : /account
app = FastAPI()

@app.post("/login",status_code=status.HTTP_302_FOUND)
def login(login_form: LoginForm):
    
    user = LoginHandler.user_log_in(login_form)
    return user

@app.post("/register",status_code=status.HTTP_201_CREATED)
def register(registration_form: RegistrationForm):
    
    RegistrationHandler.user_registration(registration_form)
    response = RedirectResponse(url='/account/activate')
    return response

@app.post("/activate/{regist_code}",status_code=status.HTTP_201_CREATED)
def activate(regist_code):
    RegistrationHandler.activate_account(regist_code)
    ...
    # user = LoginHandler.user_log_in(login_form)
    # return user