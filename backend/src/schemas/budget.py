from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class BudgetBase(BaseModel):
    category: str = Field(..., example="Groceries")
    budget_amount: float = Field(..., gt=0, example=500.00)
    start_date: datetime
    end_date: datetime

class BudgetCreate(BudgetBase):
    pass

class BudgetUpdate(BaseModel):
    category: Optional[str] = None
    budget_amount: Optional[float] = None
    actual_spent: Optional[float] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None

class BudgetResponse(BudgetBase):
    id: int
    user_id: int
    actual_spent: float
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class BudgetRecommendation(BaseModel):
    category_recommendations: dict[str, float] = Field(..., example={"Groceries": 450.00, "Utilities": 150.00})
    overall_savings_target: float = Field(..., example=200.00)
    explanation: str = Field(..., example="Recommendations based on your average spending and income over the last 3 months.")
