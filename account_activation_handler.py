from fastapi import HTTPException, status, Request
from mail_communicator import MailCommunicator
from typing import List
from py2neo_schemas.nodes import User


    
class AccountActivationHandler:
    
    @classmethod
    def send_activation_mail(self, user: User, activation_code : str, request : Request) -> bool:
        
        activation_link = "http://" + request.url.netloc + "/authentication/activate/" + activation_code
        templates = self.generate_activation_mail(user, activation_link)
        subject="[LFA] Account activation"
        recipient=user.email
        try:
            MailCommunicator.send_activation_mail(recipient, subject, templates)
        except:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Something went wrong while sending the mail"
            )

    @classmethod
    def generate_activation_mail(self, user:User, activation_link : str) -> dict:
        # return the mail created
        
        html_template = f"""
            <p>Hello <b>{user.login}</b>
            <br>This is your LFA account activation link</p>
            
            <h3>{activation_link}</h3>
		"""
        text_template = f"""
            Hello {user.login}
            This is your LFA account activation link
            
            {activation_link}
		"""
        return {
            "html_template" : html_template,
            "text_template" : text_template
        }
    
    