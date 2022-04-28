from pydantic import BaseModel
from typing import List

#-------------------------------------    AUTHENTICATION     -------------------------------
# class UserLogin(BaseModel):
#     login: str
#     password: str

class UserLoginResponse(BaseModel):
    login: str
    class Config:
        orm_mode = True

class UserRegister(BaseModel):
    login: str
    email: str
    password: str
    confirm_password: str

class UserRegisterResponse(BaseModel):
    ...

#-------------------------------------    LANDING PAGE SEARCH     -------------------------------
class Training(BaseModel):
    title: str
    description: str
    students_number: int
    mark: int
    #thumbnail: image
    author_login: str
    author_id: int

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

class TrainingCreateResponse(BaseModel):
    ...

class ChapterCreate(BaseModel):
    training_id: int
    title: str
    rank_nb: int

class ChapterCreateResponse(BaseModel):
    ...
    
class LessonCreate(BaseModel):
    chapter_id: int
    title: str
    rank_nb: int

class LessonCreateResponse(BaseModel):
    ...

class TrainingUpdate(BaseModel):
    training_id: int
    title: str 
    description: str
    thubmnail: str
    
class TrainingUpdateResponse(BaseModel):
    ...

class ChapterUpdate(BaseModel):
    chapter_id: int
    title: str

class ChapterUpdateResponse(BaseModel):
    ...

class LessonUpdate(BaseModel):
    chapter_id: int
    title: str

class LessonUpdateResponse(BaseModel):
    ...

#--------------------------------------    ANALYTICS   --------------------------------
class AnalyticsSearch(BaseModel):
    user_id: int
    content: str
    
class AnalyticsSearchResponse(BaseModel):
    ...

class AnalyticsPresence(BaseModel):
    user_id: int
    page: str
    
class AnalyticsPresenceResponse(BaseModel):
    ...

class ApplicationResponse(BaseModel):
    status: str 
    user_login: str

    class Config:
        orm_mode = True

