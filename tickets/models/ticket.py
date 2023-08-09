from sqlalchemy import Column, Integer, DateTime
from database import Base
from sqlalchemy.sql import func


class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    created_at = Column(DateTime, default=func.now())
