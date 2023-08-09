from sqlalchemy import Column, String, Integer, DateTime, Float
from database import Base
from sqlalchemy.sql import func
from pydantic import BaseModel, Field


class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    title = Column(String)
    price = Column(Float, default=0.00, )
    created_at = Column(DateTime, default=func.now())


class CreateTicketRequest(BaseModel):
    title: str = Field(min_length=5)
    price: float = Field(gt=0)

    class Config:
        json_schema_extra = {
            "example": {
                "ticket": "SolFest",
                "price": 20000.00
            }
        }
