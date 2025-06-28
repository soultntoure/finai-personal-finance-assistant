from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from ...core.database import get_db
from ...core.deps import get_current_user
from ...schemas import savings as savings_schemas
from ...models import goal as goal_models, user as user_models
from ...services.financial_rules_engine import FinancialRulesEngine

router = APIRouter()

@router.post("/savings", response_model=savings_schemas.SavingsGoalResponse, status_code=status.HTTP_201_CREATED)
async def create_savings_goal(
    savings_in: savings_schemas.SavingsGoalCreate,
    current_user: user_models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    # Create a savings goal, which is a type of financial goal
    new_goal = goal_models.Goal(
        user_id=current_user.id,
        name=savings_in.name,
        description=savings_in.description,
        target_amount=savings_in.target_amount,
        current_amount=savings_in.current_amount,
        target_date=savings_in.target_date,
        goal_type="savings"
    )
    db.add(new_goal)
    db.commit()
    db.refresh(new_goal)
    return new_goal

@router.get("/savings", response_model=List[savings_schemas.SavingsGoalResponse])
async def get_user_savings_goals(
    current_user: user_models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    # Fetch all goals of type 'savings'
    savings_goals = db.query(goal_models.Goal).filter(
        goal_models.Goal.user_id == current_user.id,
        goal_models.Goal.goal_type == "savings"
    ).all()
    return savings_goals

@router.get("/savings/suggestions", response_model=savings_schemas.SavingsSuggestion)
async def get_savings_suggestions(
    current_user: user_models.User = Depends(get_current_user),
    rules_engine: FinancialRulesEngine = Depends()
):
    # Use the rules engine to get dynamic savings suggestions based on current financial health
    suggestion = await rules_engine.get_savings_suggestion(user_id=current_user.id)
    return suggestion
