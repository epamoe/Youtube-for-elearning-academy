from py2neo_schemas.nodes import User
from fastapi import HTTPException, status
from globals import main_graph
from PIL import Image
from os import getcwd

def find_member(user_login):
    #Search for the user in the database. Returns the user if found, raise and exception otherwise
    user = User.match(main_graph,user_login).first()
    if not user.member:
        raise HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail="You are not a member"
        )
    return user

def encode_password(password) -> str:
    from passlib.context import CryptContext    
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    hashed_password = pwd_context.hash(password)
    return hashed_password

PATH_FILES = getcwd() + "/"
def resize_image(filename: str):

    sizes = [{
        "width": 500,
        "height": 500
    }]

    for size in sizes:
        size_defined = size['width'], size['height']

        image = Image.open(PATH_FILES + filename, mode="r")
        image.thumbnail(size_defined)
        image.save(PATH_FILES + str(size['height']) + "_" + filename)
