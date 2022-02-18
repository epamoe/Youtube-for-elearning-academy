
from fastapi import HTTPException, status
from neo4j import GraphDatabase
from accounts.api_classes.login_form import LoginForm
from accounts.api_classes.registration_form import RegistrationForm
from accounts.data_classes.user import User


class DBDriver:
    # Handle the effective connection with the database, and the CRUD on it
    driver = GraphDatabase.driver(uri="bolt://localhost:7687",auth=("neo4j","Renouveau"))
    session = driver.session()
    
    @classmethod
    def create_user(self, user: User) -> None:
        # Stores the user temporarily inside the database
        ...
        
    @classmethod
    def activate_user(self, user: User) -> None:
        # Activate the temporar account of a user who attempted the registration
        ...
    
    @classmethod
    def match_user(self, user: LoginForm) -> User:
        # Search for a given user in the database
        # Used for the login function
        # return the user found in the database
        ...    
        
    @classmethod    
    def is_temp_user(self, identifier:str) -> bool :
        # Verify if the account is created but not activated (the user is in the temps table)
        ...

    @classmethod    
    def is_permanent_user(self, identifier:str) -> bool :
        # Verify if the account is created but not activated (the user is in the temps table)
        ...   
        
    @classmethod
    def update_user(self, user: User) -> User:
        # update user's informations
        ...
        
    @classmethod
    def delete_user(self, user: User):
        # by admin only
        # remove an user from the site
        ...
    