from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class GoalBase(BaseModel):
    name: str = Field(..., example="Buy a House")
    description: Optional[str] = None
    target_amount: float = Field(..., gt=0, example=50000.00)
    current_amount: float = Field(default=0.0, ge=0)
    target_date: datetime
    goal_type: str = Field(..., example="savings", description="e.g., 'savings', 'debt_reduction', 'investment'")

class GoalCreate(GoalBase):
    pass

class GoalUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    target_amount: Optional[float] = None
    current_amount: Optional[float] = None
    target_date: Optional[datetime] = None
    goal_type: Optional[str] = None
    is_completed: Optional[bool] = None

class GoalResponse(GoalBase):
    id: int
    user_id: int
    is_completed: bool
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class SavingsGoalCreate(BaseModel):
    name: str = Field(..., example="Emergency Fund")
    description: Optional[str] = None
    target_amount: float = Field(..., gt=0, example=10000.00)
    current_amount: float = Field(default=0.0, ge=0)
    target_date: datetime

class SavingsGoalResponse(SavingsGoalCreate):
    id: int
    user_id: int
    is_completed: bool
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class SavingsSuggestion(BaseModel):
    suggested_amount: float = Field(..., example=150.00)
    reason: str = Field(..., example="Based on your recent spending and income patterns.")
