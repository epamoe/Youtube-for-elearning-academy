from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {
        "data" : "Hello World"
    }
    
# There is two databases for the users login
# - A permanent database for the users whom are recognized as members of the site. They are the users whom have activated
# their account
# - A temporary database for the users whom have sent their datas, but haven't yet activated it