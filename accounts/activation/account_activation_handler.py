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
    def send_activation_mail(self, user: User, activation_code : int) -> bool:
        mail_content = self.generate_activation_mail(user, activation_code)
        message = MessageSchema(
            subject="[Youtube Dev] Your activation code",
            recipients=[user.mail], # List of recipients, as many as you can pass
            body=mail_content,
            subtype="html"
        )
        MailCommunicator.send_activation_mail(message)

    @classmethod
    def generate_activation_mail(self, user:User, activation_code : str) :
        # return the mail created
        
        template = f"""
            <html>
            <body>
            

            <p>Hello {user.login}
            <br>This is your youtube dev account activation code</p>
            
            <h1>{activation_code}</h1>


            </body>
            </html>
		"""
        return template
    
    