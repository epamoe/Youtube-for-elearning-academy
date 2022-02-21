from fastapi import APIRouter, status, Depends, Response, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from starlette.responses import RedirectResponse
from accounts.api_classes.login_form import LoginForm
from accounts.api_classes.registration_form import RegistrationForm
from accounts.login.login_handler import LoginHandler
from accounts.registration.registration_handler import RegistrationHandler
from accounts import token

router = APIRouter(
    prefix="/account",
    tags= ["Authentication"]
)

@router.post("/login",status_code=status.HTTP_200_OK)
# def login(login_form: LoginForm):
def login(login_form: OAuth2PasswordRequestForm = Depends()):   
    
    # user = LoginHandler.user_log_in(login_form)
    user = LoginHandler.user_log_in(
            LoginForm(
                identifier=login_form.username,
                password=login_form.password  
                      )
        )
    # return user
    
    access_token = token.create_access_token(
        data={"sub": user.mail}
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/register",status_code=status.HTTP_201_CREATED)
def register(registration_form: RegistrationForm):
    
    RegistrationHandler.user_registration(registration_form)
    response = RedirectResponse(url='http://localhost:8000/activate')
    return response

@router.post("/activate/{regist_code}",status_code=status.HTTP_202_ACCEPTED)
def activate(regist_code):
    
    RegistrationHandler.activate_account(regist_code)