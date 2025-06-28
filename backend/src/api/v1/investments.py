from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from ...core.database import get_db
from ...core.deps import get_current_user
from ...schemas import investment as investment_schemas
from ...models import investment as investment_models, user as user_models
from ...services.ml_client_service import MLClientService

router = APIRouter()

@router.post("/investments", response_model=investment_schemas.InvestmentRecommendationResponse, status_code=status.HTTP_201_CREATED)
async def create_investment_record(
    investment_in: investment_schemas.InvestmentRecommendationCreate,
    current_user: user_models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    # In MVP, this might be saving a recommended action. In full, could track actual investments.
    new_investment_record = investment_models.InvestmentRecommendation(**investment_in.dict(), user_id=current_user.id)
    db.add(new_investment_record)
    db.commit()
    db.refresh(new_investment_record)
    return new_investment_record

@router.get("/investments/recommendations", response_model=investment_schemas.InvestmentRecommendation)
async def get_investment_recommendations(
    current_user: user_models.User = Depends(get_current_user),
    ml_service: MLClientService = Depends()
):
    # Get investment strategy recommendations from the ML service
    recommendations = await ml_service.get_investment_recommendations(user_id=current_user.id)
    return recommendations

@router.get("/investments", response_model=List[investment_schemas.InvestmentRecommendationResponse])
async def get_user_investment_records(
    current_user: user_models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    investments = db.query(investment_models.InvestmentRecommendation).filter(investment_models.InvestmentRecommendation.user_id == current_user.id).all()
    return investments
