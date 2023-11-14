from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.dependencies.db import Base


class Investment(Base):
    __tablename__ = "investments"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    platform_id = Column(String(100))
    invest_type = Column(String(50))
    name = Column(String(100))
    invested_time = Column(DateTime)
    annual_return_rate = Column(Float)
    expected_xor = Column(Float)
    volatility = Column(String(50))  # New field for volatility

    user = relationship("User", back_populates="investments")
