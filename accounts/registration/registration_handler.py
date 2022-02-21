from fastapi import HTTPException,status
from accounts.activation.account_activation_handler import AccountActivationHandler
from accounts.api_classes.registration_form import RegistrationForm
from accounts.communication.mail_communicator import MailCommunicator
from accounts.data_classes.user import User
from accounts.db_driver import DBDriver
from accounts.login.login_handler import LoginHandler
from accounts.security.Form_security_handler import FormSecurityHandler

class RegistrationHandler :
    
    @classmethod
    def user_registration(self, regist_form: RegistrationForm) -> None:
        # Handles the operations for a new user's registration
        
        r_form = regist_form
        
        user = FormSecurityHandler.validate_registration_form(r_form)
        try:
            self.verify_user_existence(user)
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, 
                detail="The user already exists"
            )
        except HTTPException:
            activation_code = self.create_new_user(user)
            self.send_validation_mail(user, activation_code)
    
    @classmethod
    def verify_user_existence(self, user:User) -> None:
        # Verifies if the user is already on the site
        try:
            LoginHandler.verify_user_existence(user.login)
        except HTTPException as e:
            try:
                LoginHandler.verify_user_existence(user.mail)
            except HTTPException as e:
                raise e
            
    @classmethod
    def create_new_user(self, user: User) -> int:
        # Stores the user temporarily inside the database
        activation_code = DBDriver.registration(user)
        return activation_code
                
    @classmethod
    def send_validation_mail(self, user: User, activation_code : int) -> None:
        AccountActivationHandler.send_activation_mail(user,activation_code)
        
    @classmethod
    def activate_account(self, registration_code : int) -> None:
        DBDriver.activate_user(registration_code)