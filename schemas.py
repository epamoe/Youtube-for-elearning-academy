from pydantic import BaseModel
from typing import List

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
    #thumbnail: image
    author_login: str

class Lesson(BaseModel):
    rank_nb: int
    title: str
    
class Chapter(BaseModel):
    title: str
    rank_nb: int
    lessons: List[Lesson]
    
class DashboardTraining(Training):
    chapters: List[Chapter]
    
class SearchResponse(BaseModel):
    training: Training
    class Config:
        orm_mode = True

class TrainingResponse(BaseModel):
    Training: DashboardTraining
    class Config:
        orm_mode = True
#--------------------------------------    USER DASHBOARD   --------------------------------
class UserUpdateLogin(BaseModel):
    login: str
    
class UserUpdateEmail(BaseModel):
    email: str

class UserUpdatePassword(BaseModel):
    password: str
    confirm_password: str

class UserUpdateProfileImage(BaseModel):
    mryz: str
    image: str # """ SHOULD BE AN IMAGE OBJECT """



#--------------------------------------    EXPERT DASHBOARD   --------------------------------
class TrainingCreate(BaseModel):
    title: str 
    description: str
    thumbnail: str

class ChapterCreate(BaseModel):
    training_uuid: str
    title: str
    rank_nb: int
    
class LessonCreate(BaseModel):
    chapter_uuid: str
    title: str
    rank_nb: int

class TrainingUpdate(BaseModel):
    uuid: str
    title: str 
    description: str
    thubmnail: str

class ChapterUpdate(BaseModel):
    uuid: str
    title: str

class LessonUpdate(BaseModel):
    uuid: str
    title: str

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

