from fastapi import HTTPException, status
from accounts.api_classes.login_form import LoginForm
from accounts.data_classes.user import User
from accounts.db_driver import DBDriver
from accounts.security.Form_security_handler import FormSecurityHandler


class LoginHandler :
    
    @classmethod
    def user_log_in(self, login_form: LoginForm) -> User:
        # Handles the operations for a user's signing in
        l_form = login_form
        
        FormSecurityHandler.securise_login_form(l_form)
        self.verify_user_existence(l_form.identifier)
        user = self.find_user(l_form)
        
        return user
    
    @classmethod
    def verify_user_existence(self, identifier: str) -> None:
        
        self.is_temp_user(identifier)
        self.is_permanent_user(identifier)
         
    @classmethod    
    def is_temp_user(self, identifier:str) -> None:
        # Verify if the account is created but not activated (the user is in the temps table)
        if(DBDriver.is_temp_user(identifier)):
            raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED, 
                    detail="The user's account isn't activated"
                )

    @classmethod    
    def is_permanent_user(self, identifier:str) -> bool :
        # Verify if the account is created and activated 
        if not DBDriver.is_permanent_user(identifier):
            raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND, 
                    detail="The user's account doesn't exists"
                )
        return True
        
    @classmethod
    def find_user(self, login_form: LoginForm) -> User:
        user = DBDriver.match_user(login_form)
        if (not user):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail="The password doesn't correspond the user"
            )
