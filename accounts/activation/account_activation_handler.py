from fastapi import HTTPException, status, Request
from accounts.communication.mail_communicator import MailCommunicator
from accounts.data_classes.user import User
from typing import List


    
class AccountActivationHandler:
    
    @classmethod
    def send_activation_mail(self, user: User, activation_code : str, request : Request) -> bool:
        # request.url.hostname
        activation_link = "http://" + request.url.netloc + "/account/activate/" + activation_code
        templates = self.generate_activation_mail(user, activation_link)
        subject="[Youtube Dev] Account activation"
        recipient=user.mail
        try:
            MailCommunicator.send_activation_mail(recipient, subject, templates)
        except:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Something went wrong when sending the mail"
            )

    @classmethod
    def generate_activation_mail(self, user:User, activation_link : str) -> dict:
        # return the mail created
        
        html_template = f"""
            <p>Hello {user.login}
            <br>This is your youtube dev account activation link</p>
            
            <h3>{activation_link}</h3>
		"""
        text_template = f"""
            Hello {user.login}
            This is your Youtube dev account activation link
            
            {activation_link}
		"""
        return {
            "html_template" : html_template,
            "text_template" : text_template
        }
    
    