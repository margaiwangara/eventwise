from pydantic import BaseModel, Field
from sqlalchemy import Column, String, Integer, DateTime, Boolean
from database import Base
from sqlalchemy.sql import func


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    is_confirmed = Column(Boolean, default=False)
    created_at = Column(DateTime, default=func.now())


class RegisterUserRequest(BaseModel):
    name: str = Field(min_length=5, max_length=50)
    email: str = Field(min_length=5, max_length=50)
    password: str = Field(min_length=8)

    class Config:
        json_schema_extra = {
            "example": {
                "name": "John Doe",
                "email": "johndoe@eventwise.dev",
                "password": "Shhhhhhhhh!!"
            }
        }


class LoginUserRequest(BaseModel):
    email: str = Field(min_length=5, max_length=50)
    password: str = Field(min_length=8)

    class Config:
        json_schema_extra = {
            "example": {
                "email": "johndoe@eventwise.dev",
                "password": "Shhhhhhhhh!!"
            }
        }
