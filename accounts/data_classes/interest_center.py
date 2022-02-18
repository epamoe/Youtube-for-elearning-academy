
from typing import List


class InterestCenter: 
    # The interest centers are the tags which will be used do propose trainings to a user 
    # e.g: html, web programming, backend, python
    
    def __init__(self, center) -> None:
        self.center = center
    
    # @classmethod
    def add_to_main_db(self):
        # Add an interest center to the interest centers db if it is not yet there
        ...
