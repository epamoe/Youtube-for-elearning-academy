from cmath import log
from accounts.api_classes.login_form import LoginForm
from fastapi import HTTPException, status
from passlib.context import CryptContext

from accounts.api_classes.registration_form import RegistrationForm
from accounts.data_classes.user import User

class FormSecurityHandler:
    
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    
    @classmethod
    def securise_login_form(self, login_form: LoginForm):
        login_form.identifier = self.securise_identifier(login_form.identifier)
        login_form.password = self.hash_password(login_form.password)
        
    @classmethod
    def validate_registration_form(self, regist_form: RegistrationForm) -> User:
        mail = self.verify_mail(regist_form.mail)
        login = self.cleanup(regist_form.login)
        password = self.verify_password(regist_form.password, regist_form.confirm_password)
        image = regist_form.profile_img
        
        user = User(mail, login, password, image)
        return user 
    
    @classmethod
    def securise_identifier(self, identifier:str) -> str:
        if self.is_email(identifier):
            return identifier
        else:
            return self.cleanup(identifier)
    
    @classmethod
    def verify_mail(self, mail:str) -> str:
        if not self.is_email(mail) :
            raise HTTPException(
                status_code=status.HTTP_406_NOT_ACCEPTABLE,
                detail="This is not an email"
            )
        return mail
    
    @classmethod
    def is_email(self, string : str) -> bool:
        # Uses REGEX to define if it is an email
        ...
        return True
        
    @classmethod
    def verify_password(self, password:str, password2:str) -> str:
        if not password == password2 :
            raise HTTPException(
                status_code=status.HTTP_406_NOT_ACCEPTABLE,
                detail="Passwords are different"
            )
        return self.hash_password(password)
        
    @classmethod
    def hash_password(self, password:str) -> str:
        return self.pwd_context.hash(password)
    
    @classmethod
    def cleanup(self, string:str) -> str:
        # Remove all tags and other to avoid code injection
        return string
