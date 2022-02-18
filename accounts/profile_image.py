
from accounts.data_classes.user import User


class ProfileImage:
    # This class contains the methods for saving a profile image, or generating 
    # one from the user's name
    @classmethod
    def create_image(self, user: str):
        # create a image generated on the base of the user's names first letters
        ...
        
    @classmethod 
    def save_image(self, user: User):
        # Save the profile image of the user passed in parameter (User.profile_img)
        ...
        
    @classmethod
    def delete_image(self, user: User):
        # Delete the profile image of the user in the database and the server
        ...