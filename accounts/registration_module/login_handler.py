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
        

        if self.is_permanent_user(l_form.identifier):
            user = self.find_user(l_form)
        elif self.is_temp_user(l_form.identifier):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, 
                detail="The user's account isn't activated"
            )
        else: 
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail="The user's account doesn't exists"
            )  
            
        return user
    
    @classmethod
    def verify_user_existence(self, identifier: str) -> bool:
        return self.is_temp_user(identifier) or self.is_permanent_user(identifier)
         
    @classmethod    
    def is_temp_user(self, identifier:str) -> bool:
        # Verify if the account is created but not activated (the user is in the temps table)
        return DBDriver.is_temp_user(identifier)

    @classmethod    
    def is_permanent_user(self, identifier:str) -> bool:
        # Verify if the account is created and activated 
        return DBDriver.is_permanent_user(identifier)
        
    @classmethod
    def find_user(self, login_form: LoginForm) -> User:
        user = DBDriver.match_user(login_form)
        if (not user):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail="The password doesn't correspond the user"
            )
        return user
