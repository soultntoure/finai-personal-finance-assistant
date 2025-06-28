from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship

from ..core.database import Base

class InvestmentRecommendation(Base):
    __tablename__ = "investment_recommendations"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    recommendation_date = Column(DateTime, server_default=func.now())
    recommended_action = Column(String, nullable=False) # e.g., 'Invest', 'Hold', 'Rebalance'
    amount = Column(Float, nullable=True) # Recommended amount to invest/save for investment
    asset_class = Column(String, nullable=True) # e.g., 'Stocks', 'Bonds', 'Crypto'
    reasoning = Column(String, nullable=True)
    # Could link to a specific financial goal
    goal_id = Column(Integer, ForeignKey("goals.id"), nullable=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    owner = relationship("User", back_populates="investment_recommendations")
    linked_goal = relationship("Goal")
