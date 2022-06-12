from fastapi import APIRouter, Depends, HTTPException,status, Request, UploadFile, File, BackgroundTasks
# from PIL import Image
# from os import getcwd
from app.functions import resize_image, PATH_FILES

from app.oauth2 import get_current_user
from .authentication import send_update_address_mail
from app import schemas
from py2neo_schemas.nodes import EmailUpdateAttempt, Training, User
from app.globals import main_graph, encodeing
from app.functions import encode_password
from email_validator import validate_email, EmailNotValidError
from typing import List

router = APIRouter(
    prefix = "/dashboard",
    tags = ["User's dashboard"]
)

@router.get("/profile", response_model = schemas.ProfileResponse)
def get_profile(user_login = Depends(get_current_user)):
    user = User.match(main_graph, user_login).first()
    
    return schemas.ProfileResponse(
        login = user.login,
        email = user.email,
        profile_img=user.profile_img,
        experiences=list(user.experiences)
    )

@router.get("/profile/{login}", response_model = schemas.ProfileResponse)
def get_profile_login(login: str):
    user = User.match(main_graph, login).first()
    if not user :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="This user doesn't exist"
        )
    return schemas.ProfileResponse(
        login = user.login,
        email = user.email,
        profile_img=user.profile_img,
        experiences=list(user.experiences)
    )
    
@router.put("/profile/login")
def update_login(new_login: schemas.UserUpdateLogin, user_login = Depends(get_current_user)):
    user = User.match(main_graph, user_login).first()
    # Let's verify if the new login proposed is already taken
    if User.match(main_graph, new_login.login).first():
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Unavailable login"
        )
    user.login = new_login.login
    main_graph.push(user)


@router.put("/profile/email")
def update_email(user_email: schemas.UserUpdateEmail, request: Request, user_login = Depends(get_current_user)):
    user = User.match(main_graph, user_login).first()
    # Let's verify if the new email proposed is valid and existing
    
    try:
        validate_email(user_email.email)
    except EmailNotValidError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Invalid or not existing email address"
        )

    # Let's ensure that new email proposed isn't already taken
    if User.match(main_graph).where("_.email='"+user_email.email+"'").first():
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Unavailable email"
        )
        
    attempt = EmailUpdateAttempt(email = user_email.email)
    user.email_update_attempt.add(attempt)
    send_update_address_mail(user, user_email.email, request)
    main_graph.push(user)

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

    attempt = EmailUpdateAttempt.match(main_graph,strd).first()
    if attempt :
        user = list(attempt.user)[0]
        user.email = attempt.email
        main_graph.delete(attempt)
        main_graph.push(user)
    else: 
        raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED, 
                    detail="Invalid activation link"
            )


@router.put("/profile/password")
def update_password(user_password: schemas.UserUpdatePassword, user_login = Depends(get_current_user)):
    user = User.match(main_graph, user_login).first()
    
    from passlib.context import CryptContext
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    same_password = pwd_context.verify(user_password.current_password, user.password)
    if not same_password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Incorrect current password"
        )
    if user_password.password != user_password.confirm_password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="The password and the confirmation password don't match"
        )

    hashed_password = encode_password(user_password.password)
    user.password = hashed_password
    main_graph.push(user)


@router.put("/profile/profile_image")
async def update_profile_image(background_tasks: BackgroundTasks, file: UploadFile = File(...)):

    # SAVE FILE ORIGINAL
    with open(PATH_FILES + file.filename, "wb") as myfile:
        content = await file.read()
        print(content)
        # myfile.write(content)
        myfile.close()

    # RESIZE IMAGES
    # background_tasks.add_task(resize_image, filename=file.filename)


@router.get("/notifications/", response_model = List[schemas.Notification])
def get_notifications(user_login = Depends(get_current_user)):
    user = User.match(main_graph, user_login).first()
    return list(user.notifications)

@router.get("/profile/trainings/", response_model = List[schemas.UserTrainingResponse])
def get_trainings(user_login = Depends(get_current_user)):
    user = User.match(main_graph, user_login).first()
    trainings = list(user.follow_training)
    response = [{
        "training" : schemas.Training(
            uuid = train.uuid,
            title = train.title,
            description = train.description,
            students_number = train.students_number,
            mark = train.mark,
            thumbnail = train.thumbnail,
            author_login = list(train.publisher)[0].login
        ),
        "progression" : user.follow_training.get(train,"progression")
    } for train in trainings]

    return response


    
@router.get("/user/training/follow/{uuid}")
def follow_training(uuid: str, user_login = Depends(get_current_user)):
    user = User.match(main_graph, user_login).first()
    training = Training.match(main_graph).where("_.uuid='"+uuid+"'").first()
    user.follow_training.add(training, properties={
        "progression": 0
    })
    main_graph.push(user)
    
@router.get("/expert/apply", status_code=status.HTTP_200_OK)
def apply(user_login = Depends(get_current_user)):
    user_node = User.match(main_graph, user_login).first()
    if user_node.did_apply():
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="This user already applied to become a member")
    user_node.apply()
    main_graph.push(user_node)
    