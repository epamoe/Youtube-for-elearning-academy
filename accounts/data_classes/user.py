from pydantic import BaseModel
from typing import Any, Optional

class User(BaseModel) :
    # This class contains the informations of an user
    
    mail: str
    login: str
    password: str
    profile_img: Optional[str]
    
    def __init__(__pydantic_self__, **data: Any) -> None:
        super().__init__(**data)
        
    