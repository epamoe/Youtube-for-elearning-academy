from pydantic import BaseModel
from typing import Any

class User(BaseModel) :
    # This class contains the informations of an user
    # It is a data class, not a functionnal one
    
    mail: str
    login: str
    password: str
    profile_img: str
    
    def __init__(__pydantic_self__, **data: Any) -> None:
        super().__init__(**data)