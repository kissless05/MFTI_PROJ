# app/main.py
from fastapi import FastAPI
from app import models
from app.database import engine
from app.routers import users, applications
from app import auth
from app.routers import reviews



models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(applications.router)
app.include_router(auth.router)
app.include_router(reviews.router)

@app.get("/")
def root():
    return {"message": "База подключена и всё работает!"}

