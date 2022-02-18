
from typing import Any, List
from accounts.data_classes.interest_center import InterestCenter
from accounts.data_classes.user import User
from trainings.training import Training


class Member(User):
    
    # For one user we know all his interest centers
    interest_centers : List[InterestCenter]
    # For one user we know all the trainings he is following
    trainings: List[Training]
    
    def __init__(__pydantic_self__, **data: Any) -> None:
        super().__init__(**data)
        
    def append_center(self, center: str): 
        # add one interest center to the list
        ...
        
    def follow_training(self, training: Training):
        # add the training to the member's trainings list
        ...
    
    def abort_training(self, training: Training):
        # remove a training and the progress informations associated for a member
        ...
        
    
    ...