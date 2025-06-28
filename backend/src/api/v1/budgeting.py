from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from ...core.database import get_db
from ...core.deps import get_current_user
from ...schemas import budget as budget_schemas
from ...models import budget as budget_models, user as user_models
from ...services.ml_client_service import MLClientService

router = APIRouter()

@router.post("/budgets", response_model=budget_schemas.BudgetResponse, status_code=status.HTTP_201_CREATED)
async def create_budget(
    budget_in: budget_schemas.BudgetCreate,
    current_user: user_models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    # Basic budget creation. ML service could provide initial recommendations.
    new_budget = budget_models.Budget(**budget_in.dict(), user_id=current_user.id)
    db.add(new_budget)
    db.commit()
    db.refresh(new_budget)
    return new_budget

@router.get("/budgets", response_model=List[budget_schemas.BudgetResponse])
async def get_user_budgets(
    current_user: user_models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    budgets = db.query(budget_models.Budget).filter(budget_models.Budget.user_id == current_user.id).all()
    return budgets

@router.get("/budgets/recommendations", response_model=budget_schemas.BudgetRecommendation)
async def get_budget_recommendations(
    current_user: user_models.User = Depends(get_current_user),
    ml_service: MLClientService = Depends()
):
    # Request budget recommendations from the ML service
    recommendations = await ml_service.get_budget_recommendations(user_id=current_user.id)
    return recommendations
