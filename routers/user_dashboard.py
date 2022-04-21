from fastapi import APIRouter
import schemas
router = APIRouter(
    prefix = "/ydev/dashboard",
    tags = ["User's dashboard"]
)

@router.get("/profile/get")
def get_profile():
    ...
    
@router.put("/profile/update/login")
def update_login(user_login: schemas.UserUpdateLogin):
    return user_login

@router.put("/profile/update/email")
def update_email(user_email: schemas.UserUpdateEmail):
    return user_email

@router.put("/profile/update/password")
def update_password(user_password: schemas.UserUpdatePassword):
    return user_password

@router.put("/profile/update/profile_image")
def update_profile_image(user_profile_image: schemas.UserUpdateProfileImage):
    return user_profile_image

@router.get("/profile/expert/get/{id}")
def get_expert_profile(id):
    ...

@router.get("/analytics/lesson/{id}")
def analytic_lesson(id):
    ...

@router.get("/analytics/video/{id}")
def analytic_video(id):
    ...
    
@router.get("/notifications/get/")
def get_notifications():
    ...
    
@router.get("/user/trainings/get/")
def get_trainings():
    ...
    
@router.get("/user/training/follow/")
def follow_training():
    ...
    
@router.post("/expert/apply")
def apply(data: schemas.UserApply):
    return data
    