from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.dependencies.db import Base


class Relationship(Base):
    __tablename__ = "relationships"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    relative_id = Column(Integer, ForeignKey('users.id'))
    relationship_type = Column(String(50))
    can_view_portfolio = Column(Boolean, default=False)

    user = relationship("User", foreign_keys=[user_id])
    relative = relationship("User", foreign_keys=[relative_id])
