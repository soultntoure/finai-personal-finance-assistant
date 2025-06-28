from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class InvestmentRecommendationBase(BaseModel):
    recommended_action: str = Field(..., example="Invest") # e.g., 'Invest', 'Hold', 'Rebalance'
    amount: Optional[float] = Field(None, gt=0, example=500.00)
    asset_class: Optional[str] = Field(None, example="S&P 500 ETF")
    reasoning: Optional[str] = None
    goal_id: Optional[int] = None # Link to a financial goal

class InvestmentRecommendationCreate(InvestmentRecommendationBase):
    pass

class InvestmentRecommendationResponse(InvestmentRecommendationBase):
    id: int
    user_id: int
    recommendation_date: datetime
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class InvestmentRecommendation(BaseModel):
    strategy_type: str = Field(..., example="Balanced Growth")
    suggested_allocations: dict[str, float] = Field(..., example={"Stocks": 0.6, "Bonds": 0.3, "Cash": 0.1})
    projected_returns: float = Field(..., example=0.07)
    risk_level: str = Field(..., example="Medium")
    explanation: str = Field(..., example="Based on your financial goals and current market conditions, a balanced growth strategy is recommended.")
