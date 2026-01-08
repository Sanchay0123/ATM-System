from sqlalchemy import Column, Integer, String, Float
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    card_number = Column(String, unique=True)
    pin = Column(String)
    balance = Column(Float)
