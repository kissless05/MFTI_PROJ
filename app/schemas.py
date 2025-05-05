
# app/schemas.py

from pydantic import BaseModel, EmailStr
from typing import Optional

# Для пользователей
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class User(BaseModel):
    id: int
    email: EmailStr

    class Config:
        from_attributes = True

# Для логина и токена
class Token(BaseModel):
    access_token: str
    token_type: str

# Для Applications
class ApplicationBase(BaseModel):
    title: str
    content: Optional[str] = None

class ApplicationCreate(ApplicationBase):
    title: str
    content: Optional[str] = None

class Application(ApplicationBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True

# Для Review (третья таблица)
class ReviewBase(BaseModel):
    rating: int
    comment: Optional[str] = None

class ReviewCreate(ReviewBase):
    application_id: int

class Review(ReviewBase):
    id: int
    application_id: int
    reviewer_id: int

    class Config:
        from_attributes = True

class UserOut(BaseModel):
    id: int
    email: EmailStr

    class Config:
        from_attributes = True

class ApplicationOut(ApplicationBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True