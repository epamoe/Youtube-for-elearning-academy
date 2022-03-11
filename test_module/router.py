

from fastapi.security import OAuth2PasswordRequestForm
from fastapi import APIRouter,status,Depends
from accounts import token

from accounts.activation.account_activation_handler import AccountActivationHandler
from accounts.api_classes.login_form import LoginForm
from accounts.data_classes.user import User
from accounts.registration_module.login_handler import LoginHandler


router = APIRouter(
    prefix="/tests",
    tags= ["tests"]
)

@router.get("/login",status_code=status.HTTP_200_OK)
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

@router.get("/{id}")
def test(registration_id : str, email: str):
    try:
        AccountActivationHandler.send_activation_mail(
            User(
                mail=email,
                login="icono",
                password="string",
                profile_img="string"
            ),
            registration_id
        )
        return {
            "message" : "Finished"
        }
    except Exception as e:
        return "Error"