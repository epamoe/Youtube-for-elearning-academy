from pydantic import BaseModel
from typing import List, Optional

#-------------------------------------    AUTHENTICATION     -------------------------------

class UserLoginResponse(BaseModel):
    login: str
    class Config:
        orm_mode = True

class UserRegister(BaseModel):
    login: str
    email: str
    password: str
    confirm_password: str

#-------------------------------------    LANDING PAGE SEARCH     -------------------------------
class Training(BaseModel):
    uuid: str
    title: str
    description: str
    students_number: int
    mark: int
    thumbnail: str
    author_login: str

    class Config:
        orm_mode = True
        
class Lesson(BaseModel):
    uuid: Optional[str]
    rank_nb: int
    title: str
    
    class Config:
        orm_mode = True

class Chapter(BaseModel):
    uuid: Optional[str]
    title: str
    rank_nb: int
    lessons: List[Lesson]
    
    # class Config:
    #     orm_mode = True

class DashboardTraining(Training):
    chapters: List[Chapter]

    class Config:
        orm_mode = True

#--------------------------------------    USER DASHBOARD   --------------------------------
class Experience(BaseModel):
    key: str
    value: str

class ProfileResponse(BaseModel):
    login: str
    email: str
    profile_img: str #image value
    experiences: List[Experience]
    class Config:
        orm_mode = True
class UserUpdateLogin(BaseModel):
    login: str
    
class UserUpdateEmail(BaseModel):
    email: str

class UserUpdatePassword(BaseModel):
    current_password: str
    password: str
    confirm_password: str

class UserUpdateProfileImage(BaseModel):
    mryz: str
    image: str # """ SHOULD BE AN IMAGE OBJECT """

class Notification(BaseModel):
    uuid: str
    content: str
    class Config:
        orm_mode = True

class UserTrainingResponse(BaseModel):
    training: Training
    progression: float
    class Config:
        orm_mode = True
#--------------------------------------    EXPERT DASHBOARD   --------------------------------

class TrainingCreate(BaseModel):
    title: str 
    description: str
    thumbnail: str

class ChapterCreate(BaseModel):
    training_uuid: int
    title: str
    rank_nb: int
    
class LessonCreate(BaseModel):
    chapter_uuid: int
    title: str
    rank_nb: int

class TrainingUpdate(BaseModel):
    training_uuid: int
    title: str 
    description: str
    thubmnail: str

class ChapterUpdate(BaseModel):
    chapter_uuid: int
    title: str
    rank_nb: int

class LessonUpdate(BaseModel):
    lesson_uuid: int
    title: str
    rank_nb: int

#--------------------------------------    LEARNING PAGE   --------------------------------
class Video(BaseModel):
    video_id: str
    title: str
    viewCount: str
    channel_name: str
    # channel_id: str
    description: str
    class Config:
        orm_mode = True
#--------------------------------------    ANALYTICS   --------------------------------
class AnalyticsSearch(BaseModel):
    content: str

class AnalyticsPresence(BaseModel):
    page: str

class ApplicationResponse(BaseModel):
    uuid: str
    status: str 
    user_login: str

    class Config:
        orm_mode = True

