
from fastapi import HTTPException, status
from neo4j import GraphDatabase
from accounts.api_classes.login_form import LoginForm
from accounts.data_classes.user import User
from accounts.security.Form_security_handler import FormSecurityHandler


class DBDriver:
    # Handle the effective connection with the database, and the CRUD on it
    driver = GraphDatabase.driver(uri="bolt://localhost:7687",auth=("neo4j","Renouveau"))
    session = driver.session()
    
    @classmethod
    def create_user(self, user: User) -> None:
        # Stores the user permanently inside the database
        query = """
        CREATE (a: User{mail:$mail,login:$login,password:$password,profile_img:$profile_img}) return a
        """
        datas = {
            "mail": user.mail,
            "login": user.login,
            "password" : user.password,
            "profile_img" : user.profile_img
        }
        self.session.run(query,datas)
    @classmethod
    def registration(self, user: User) -> int:
        activation_code = self.create_temp_user(user)
        return activation_code
        
    @classmethod
    def create_temp_user(self, user: User) -> int:
        # Create a temporar user in the database
        regist_id = self.get_next_activation_code()
        query = """
        CREATE (r: RegistrationAttempt{regist_id:$regist_id})-[:FOR_USER]->(a: TempUser{mail:$mail,login:$login,password:$password,profile_img:$profile_img}) return a
        """
        datas = {
            "regist_id": regist_id,
            "mail": user.mail,
            "login": user.login,
            "password" : user.password,
            "profile_img" : user.profile_img
        }
        self.session.run(query,datas)
        return regist_id
    
    @classmethod    
    def delete_temp_user(self, user: User) -> None:
        # Delete a temporar user and his registration attempt node, to cancel his registration
        query = """
        MATCH (r:RegistrationAttempt)-[f:FOR_USER]->(t:TempUser) WHERE t.mail=$mail
        DELETE r,f,t
        """
        datas = {
            "mail": user.mail
        }
        self.session.run(query,datas)
    
    @classmethod
    def get_next_activation_code(self):
        query = """
        MATCH (r:RegistrationAttempt),(u:User) return COUNT(r) + COUNT(u) AS number
        """
        response = self.session.run(query)
        result = response.single()["number"] # The total number of users in the site, registered or not
        
        return result + 1
        
    @classmethod
    def activate_user(self, registration_code: int) -> None:
        # Activate the temporar account of a user who attempted the registration
        if self.is_valid_registration_code(registration_code) :
            query = """
            MATCH (r:RegistrationAttempt)-[f:FOR_USER]->(t:TempUser) WHERE r.regist_id=toInteger($registration_code)
            SET t:User
            REMOVE t:TempUser
            DELETE r,f
            """
            datas = {
                "registration_code": registration_code
            }
            self.session.run(query,datas)
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail= "Not corresponding registration code"
                )    
        
    @classmethod
    def is_valid_registration_code(self, code: int) -> bool:
        
        query = """
        MATCH (r:RegistrationAttempt) WHERE r.regist_id=toInteger($registration_code) RETURN COUNT(r) AS number
        """
        datas = {
            "registration_code": code
        }
        response = self.session.run(query,datas)
        result = response.single()["number"]
        if result == 0:
            return False
        else : 
            return True
    
    @classmethod
    def match_user(self, user: LoginForm) -> User:
        # Search for a given user in the database
        # Used for the login function
        # return the user found in the database
        query = """
        MATCH (u:User) WHERE (u.mail = $identifier OR u.login = $identifier) RETURN u
        """
        datas = {
            "identifier": user.identifier
        }
        response = self.session.run(query,datas)
        # This is the Users objects list
        users_result = [User(mail=record[0]["mail"],login=record[0]["login"],password=record[0]["password"],profile_img=record[0]["profile_img"]) for record in response]
        if FormSecurityHandler.pswd_hash_compare(users_result[0].password, user.password):
            return users_result[0]  
        return None
        
    @classmethod    
    def is_temp_user(self, identifier:str) -> bool :
        query = """
        MATCH (u:TempUser) WHERE u.mail = $identifier OR u.login = $identifier return count(u) as number
        """
        datas = {
            "identifier": identifier
        }
        response = self.session.run(query,datas)
        result = response.single()["number"]
        if(result == 0):
            return False
        else: 
            return True

    @classmethod    
    def is_permanent_user(self, identifier:str) -> bool :
        query = """
        MATCH (u:User) WHERE u.mail = $identifier OR u.login = $identifier return count(u) as number
        """
        datas = {
            "identifier": identifier
        }
        response = self.session.run(query,datas)
        result = response.single()["number"]
        if(result == 0):
            return False
        else : 
            return True
        
    @classmethod
    def update_user(self, user: User) -> User:
        # update user's informations
        ...
        
    @classmethod
    def delete_user(self, user: User):
        # by admin only
        # remove an user from the site
        ...
    