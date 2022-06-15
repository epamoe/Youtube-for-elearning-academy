from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import (admin_dashboard, analytics, authentication,
                    expert_dashboard, landing_page_search, learning_page,
                    user_dashboard)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_methods = ["*"],
    allow_credentials = True,
    allow_headers = ["*"]
)  

app.include_router(authentication.router)
app.include_router(admin_dashboard.router)
app.include_router(analytics.router)
app.include_router(learning_page.router)
app.include_router(user_dashboard.router)
app.include_router(expert_dashboard.router)
app.include_router(landing_page_search.router)

@app.get("/")
def root():
    return {"message": "Refactoring ongoing "}







