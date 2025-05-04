# app/main.py
from fastapi import FastAPI
from app import models
from app.database import engine
from app.routers import users, applications, reviews
from app import auth
from app.database import get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(applications.router)
app.include_router(auth.router)
app.include_router(reviews.router)

@app.get("/")
def root():
    return {"message": "База подключена и всё работает!"}


