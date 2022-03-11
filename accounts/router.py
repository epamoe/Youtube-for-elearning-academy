from fastapi import APIRouter, status, Depends, Request,HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from starlette.responses import RedirectResponse
from accounts.api_classes.login_form import LoginForm
from accounts.api_classes.registration_form import RegistrationForm
from accounts.db_driver import DBDriver
from accounts.registration_module.login_handler import LoginHandler
from accounts.registration_module.registration_handler import RegistrationHandler
from accounts import token
import os
from accounts.security.Form_security_handler import FormSecurityHandler
from dotenv import load_dotenv
load_dotenv()

app_domain = os.getenv("APP_DOMAIN")

router = APIRouter(
    tags= ["Authentication"]
)

@router.post("/login",status_code=status.HTTP_200_OK)
def login(login_form: OAuth2PasswordRequestForm = Depends()):       
    user = LoginHandler.user_log_in(
            LoginForm(
                identifier=login_form.username,
                password=login_form.password  
                      )
        )
    access_token = token.create_access_token(
        data={"sub": user.mail}
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/register",status_code=status.HTTP_201_CREATED)
def register(registration_form: RegistrationForm, request: Request):
    
    RegistrationHandler.user_registration(registration_form, request)
    return {
        "message" : "Registration successful"
    }

@router.get("/activate/{regist_code}",status_code=status.HTTP_202_ACCEPTED)
def activate(regist_code:str):
    RegistrationHandler.activate_account(regist_code)
    response = RedirectResponse(url='http://' + app_domain + '/login')
    return response

@router.get("/verify/login/{login}",status_code=status.HTTP_200_OK)
def search_login(login:str):
    if DBDriver.login_already_taken(login):
        raise HTTPException(
            status_code=status.HTTP_226_IM_USED,
            detail="login already used"
        )
    return {
        "message" : "login available"
    }

@router.get("/verify/email/{email}",status_code=status.HTTP_200_OK)
def search_email(email:str):
    if DBDriver.email_already_taken(email) or not FormSecurityHandler.is_email(email):
        raise HTTPException(
            status_code=status.HTTP_226_IM_USED,
            detail="email invalid or already used"
        )
    return {
        "message" : "email available"
    }