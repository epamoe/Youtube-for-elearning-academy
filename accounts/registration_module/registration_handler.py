from fastapi import HTTPException,status
from accounts.activation.account_activation_handler import AccountActivationHandler
from accounts.api_classes.registration_form import RegistrationForm
from accounts.communication.mail_communicator import MailCommunicator
from accounts.data_classes.user import User
from accounts.db_driver import DBDriver
from login_handler import LoginHandler
from accounts.security.Form_security_handler import FormSecurityHandler

class RegistrationHandler :
    
    @classmethod
    def user_registration(self, regist_form: RegistrationForm) -> None:
        # Handles the operations for a new user's registration
        
        r_form = regist_form
        
        user = FormSecurityHandler.validate_registration_form(r_form)
        if self.verify_user_existence(user) : 
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, 
                detail="The user already exists"
            )
        else:
            try: 
                activation_code = self.create_new_user(user)
                self.send_activation_mail(user, activation_code)
            except Exception as e:
                self.cancel_user_registration(user)
                raise e
    @classmethod
    def cancel_user_registration(self, user:User):
        # cancels the user's registration attempt by removing his informations in the database
        DBDriver.delete_temp_user(user)
        
    @classmethod
    def verify_user_existence(self, user:User) -> bool:
        # Verifies if the user is already on the site
        # It looks if the login is already taken, or if the email is already used
        return LoginHandler.verify_user_existence(user.login) or LoginHandler.verify_user_existence(user.mail)
            
    @classmethod
    def create_new_user(self, user: User) -> int:
        # Stores the user temporarily inside the database
        try:
            activation_code = DBDriver.registration(user)
        except:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Something went wrong while registering the user"
            )
        return activation_code
                
    @classmethod
    def send_activation_mail(self, user: User, activation_code : int) -> None:
        AccountActivationHandler.send_activation_mail(user,activation_code)
        
    @classmethod
    def activate_account(self, registration_code : int) -> None:
        DBDriver.activate_user(registration_code)