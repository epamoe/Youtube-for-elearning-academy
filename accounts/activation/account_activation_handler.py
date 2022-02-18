from accounts.data_classes.user import User


class AccountActivationHandler:
    
    @classmethod
    def send_activation_mail(self, user: User) -> bool:
        link = self.generate_activation_link(user)
        ...
        
    @classmethod
    def generate_activation_link(self, user) -> str: 
        # This function generates an activation link 
        ...
        
