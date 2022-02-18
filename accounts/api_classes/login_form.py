from pydantic import BaseModel


class LoginForm(BaseModel):
    # The user log to his account by entering either his pseudo or his email
    # This data is stored inside the identifier attribute
    identifier : str 
    password : str
