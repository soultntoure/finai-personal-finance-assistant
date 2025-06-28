from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship

from ..core.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    transactions = relationship("Transaction", back_populates="owner")
    budgets = relationship("Budget", back_populates="owner")
    goals = relationship("Goal", back_populates="owner")
    investment_recommendations = relationship("InvestmentRecommendation", back_populates="owner")
