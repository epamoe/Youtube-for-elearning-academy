from fastapi_mail import FastMail, MessageSchema,ConnectionConfig
from pydantic import EmailStr, BaseModel
from typing import List



# class EmailSchema(BaseModel):
#    email: List[EmailStr]
   

   
class MailCommunicator: 
    conf = ConnectionConfig(
        MAIL_USERNAME="ytbdev10@gmail.com",
        MAIL_PASSWORD="Ycono10@2222",
        MAIL_PORT=587,
        MAIL_SERVER="smtp.gmail.com",
        MAIL_TLS=True,
        MAIL_SSL=False
        )
    
    @classmethod
    async def send_activation_mail(self, message: MessageSchema) -> None:
        # create the activation link and send it to user's mail address
        fm = FastMail(self.conf)
        await fm.send_message(message)
        