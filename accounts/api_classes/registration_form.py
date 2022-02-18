from typing import Any
from pydantic import BaseModel


class RegistrationForm(BaseModel):
    login : str 
    mail : str 
    password : str
    confirm_password: str
    profile_img : str

    def __init__(__pydantic_self__, **data: Any) -> None:
        super().__init__(**data)