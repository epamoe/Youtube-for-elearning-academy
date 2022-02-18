

from accounts.data_classes.user import User


class MailCommunicator: 
    
    @classmethod
    def send_activation_mail(self, email: User) -> bool:
        # create the activation link and send it to user's mail address
        ...
        
    @classmethod
    def generate_activation_mail(self, link:str, address : str) :
        # return the mail created
        ...
        
    @classmethod
    def generate_activation_link(self, user : User) :
        # return the mail created
        ...