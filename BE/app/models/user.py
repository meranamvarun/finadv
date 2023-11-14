from sqlalchemy import Column, Integer, String, Text
from app.dependencies.db import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    password_hash = Column(String(255))
    email = Column(String(100), index=True)
    contact_number = Column(String(15))
    comm_address = Column(Text)
    home_address = Column(Text)
    investments = relationship("Investment", back_populates="user")
