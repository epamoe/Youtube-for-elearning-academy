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
            MailCommunicator.send_mail(recipient, subject, templates)
        except:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Something went wrong while sending the mail"
            )

    @classmethod
    def send_update_address_mail(self, user: User, activation_code : str, recipient_address: str, request : Request) -> bool:
        
        activation_link = "http://" + request.url.netloc + "/dashboard/profile/email/confirm/" + activation_code
        templates = self.generate_update_address_mail(user, activation_link)
        subject="[LFA] Account email address update"
        recipient=recipient_address
        try:
            MailCommunicator.send_mail(recipient, subject, templates)
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
        
    @classmethod
    def generate_update_address_mail(self, user:User, update_address_link : str) -> dict:
        
        html_template = f"""
            <p>Hello <b>{user.login}</b>
            <br>You've attempted to replace your LFA account email address by this one. Click on the link bellow to validate it, of just ignore it if you are not {user.login}</p>
            
            <h3>{update_address_link}</h3>
		"""
        text_template = f"""
            Hello {user.login}
            You've attempted to replace your LFA account email address by this one. Click on the link bellow to validate it, of just ignore it if you are not {user.login}
            
            {update_address_link}
		"""
        return {
            "html_template" : html_template,
            "text_template" : text_template
        }
    
    