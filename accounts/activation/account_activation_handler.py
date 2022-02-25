import profile
from fastapi import FastAPI
from accounts.communication.mail_communicator import MailCommunicator
from accounts.data_classes.user import User
from fastapi import FastAPI
from fastapi_mail import FastMail, MessageSchema,ConnectionConfig
from starlette.requests import Request
from starlette.responses import JSONResponse
from pydantic import EmailStr, BaseModel
from typing import List


    
class AccountActivationHandler:
    
    @classmethod
    def send_activation_mail(self, user: User, activation_code : str) -> bool:
        templates = self.generate_activation_mail(user, activation_code)
        subject="[Youtube Dev] Your activation code"
        recipient=user.mail

        MailCommunicator.send_activation_mail(recipient, subject, templates)

    @classmethod
    def generate_activation_mail(self, user:User, activation_code : str) -> dict:
        # return the mail created
        
        html_template = f"""
            <p>Hello {user.login}
            <br>This is your youtube dev account activation code</p>
            
            <h1>{activation_code}</h1>
		"""
        text_template = f"""
            Hello {user.login}
            This is your Youtube dev account activation code
            
            {activation_code}
		"""
        return {
            "html_template" : html_template,
            "text_template" : text_template
        }
    
    