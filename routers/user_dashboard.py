from fastapi import APIRouter, Depends, HTTPException,status, Request
from oauth2 import get_current_user
from routers.authentication import send_update_address_mail
import schemas
from py2neo_schemas.nodes import EmailUpdateAttempt, User
from globals import graph
from globals import encodeing

router = APIRouter(
    prefix = "/dashboard",
    tags = ["User's dashboard"]
)

@router.get("/profile")
def get_profile():
    ...

@router.get("/profile/{login}")
def get_profile():
    ...
    
@router.put("/profile/login")
def update_login(new_login: schemas.UserUpdateLogin, user_login = Depends(get_current_user)):
    user = User.match(graph, user_login).first()
    # Let's verify if the new login proposed is already taken
    if User.match(graph, new_login.login).first():
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Unavailable login"
        )
    user.login = new_login.login
    graph.push(user)


@router.put("/profile/email")
def update_email(user_email: schemas.UserUpdateEmail, request: Request, user_login = Depends(get_current_user)):
    user = User.match(graph, user_login).first()
    # Let's verify if the new email proposed is valid and existing
    from email_validator import validate_email, EmailNotValidError
    try:
        validate_email(user_email.email)
    except EmailNotValidError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Invalid or not existing email address"
        )

    # Let's ensure that new email proposed isn't already taken
    if User.match(graph).where("_.email='"+user_email.email+"'").first():
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Unavailable email"
        )
        
    attempt = EmailUpdateAttempt(email = user_email.email)
    user.email_update_attempt.add(attempt)
    send_update_address_mail(user, user_email.email, request)
    graph.push(user)

@router.get("/profile/email/confirm/{confirmation_code}")
async def confirm(confirmation_code:str):    
    strd = None
    try:
        import base64
        strd = confirmation_code.encode(encodeing)
        strd = base64.b64decode(strd)
        strd = strd.decode(encodeing)
    except:
        raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED, 
                    detail="Invalid activation link"
            )

    attempt = EmailUpdateAttempt.match(graph,strd).first()
    if attempt :
        user = list(attempt.user)[0]
        user.email = attempt.email
        graph.delete(attempt)
        graph.push(user)
    else: 
        raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED, 
                    detail="Invalid activation link"
            )


@router.put("/profile/password")
def update_password(user_password: schemas.UserUpdatePassword):
    return user_password

@router.put("/profile/profile_image")
def update_profile_image(user_profile_image: schemas.UserUpdateProfileImage):
    return user_profile_image

@router.get("/profile/expert/{id}")
def get_expert_profile(id):
    ...

@router.get("/notifications/")
def get_notifications():
    ...
    
@router.get("/profile/trainings/")
def get_trainings():
    ...
    
@router.get("/user/training/follow/")
def follow_training():
    ...
    
@router.get("/expert/apply", status_code=status.HTTP_200_OK)
def apply(user_login = Depends(get_current_user)):
    user_node = User.match(graph, user_login).first()
    if user_node.did_apply():
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="This user already applied to become a member")
    user_node.apply()
    graph.push(user_node)
    