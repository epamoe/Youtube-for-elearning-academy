from fastapi import APIRouter, status
from fastapi import status,HTTPException, Depends, Request
from schemas import UserRegister
from fastapi.security import OAuth2PasswordRequestForm
import token_handler 
from account_activation_handler import AccountActivationHandler
from py2neo_schemas.nodes import User
from globals import main_graph ,encodeing
from functions import encode_password
from email_validator import validate_email, EmailNotValidError
from passlib.context import CryptContext

router = APIRouter(
    prefix = "",
    tags = ["Authentication"]
)



@router.post("/register", status_code=status.HTTP_200_OK)
async def register(regist_form: UserRegister, request : Request):
    if regist_form.password != regist_form.confirm_password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="The password and the confirmation password don't match"
        )

    try:
        validate_email(regist_form.email)
    except EmailNotValidError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Invalid or not existing email"
        )

    login = regist_form.login.lower()
    email = regist_form.email.lower()
        
    user = save_user(login, email, regist_form.password)
    try:
        send_activation_mail(user, request)
    except Exception as e:
        main_graph.delete(user)
        raise e
    

@router.post("/login", status_code=status.HTTP_200_OK)
async def login(login_form: OAuth2PasswordRequestForm = Depends()): 
    username = login_form.username.lower()
    
    user = find_user(username, login_form.password)
    if user:
        if user.activated: 
            access_token = token_handler.create_access_token(
                data={"sub": user.login}
            )
            user_type = None
            if user.member:
                user_type = "member"
            elif user.admin:
                user_type = "admin"
            else:
                user_type = "user"

            return {"access_token": access_token, "token_type": "bearer", "user_type": user_type}
        else: 
            raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED, 
                    detail="This user account isn't yet activated. Look for the activation link in your mail box"
            )
    else: 
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="The user doesn't exists"
        )

@router.get("/activate/{registration_code}")
async def activate(registration_code:str):    
    strd = None
    try:
        import base64
        strd = registration_code.encode(encodeing)
        strd = base64.b64decode(strd)
        strd = strd.decode(encodeing)
    except:
        raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED, 
                    detail="Invalid activation link"
            )
    user = User.match(main_graph,strd).first()
    if user :
        user.activated = True
        main_graph.push(user)
    else: 
        raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED, 
                    detail="Invalid activation link"
            )


def find_user(login, password):
    user = User.match(main_graph).where(f"_.email = '{login}' OR _.login = '{login}'").first()
    if not user: 
        return False    

    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    same_password = pwd_context.verify(password, user.password)
    if same_password:
        return user 
    else: 
        return None


def save_user(login, email, password):

    user = User.match(main_graph).where(f"_.login = '{login}' OR _.email = '{email}'").first()

    if user :
        raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, 
                detail="The user already exists"
        )
    else:
        hashed_password = encode_password(password)
        user = User(login=login, email=email, password = hashed_password, profile_img = None) 
        main_graph.push(user)
    return user


def send_activation_mail(user,request):
    import base64

    strc = user.login
    str_enc = strc.encode(encodeing)
    str_enc = base64.b64encode(str_enc)
    str_enc = str_enc.decode(encodeing)

    AccountActivationHandler.send_activation_mail(user,str_enc,request)
    
def send_update_address_mail(user,new_address,request):
    import base64

    strc = new_address
    str_enc = strc.encode(encodeing)
    str_enc = base64.b64encode(str_enc)
    str_enc = str_enc.decode(encodeing)

    AccountActivationHandler.send_update_address_mail(user,str_enc,new_address,request)
    