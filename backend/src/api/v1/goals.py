from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from ...core.database import get_db
from ...core.deps import get_current_user
from ...schemas import goal as goal_schemas
from ...models import goal as goal_models, user as user_models

router = APIRouter()

@router.post("/goals", response_model=goal_schemas.GoalResponse, status_code=status.HTTP_201_CREATED)
async def create_financial_goal(
    goal_in: goal_schemas.GoalCreate,
    current_user: user_models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    new_goal = goal_models.Goal(**goal_in.dict(), user_id=current_user.id)
    db.add(new_goal)
    db.commit()
    db.refresh(new_goal)
    return new_goal

@router.get("/goals", response_model=List[goal_schemas.GoalResponse])
async def get_user_financial_goals(
    current_user: user_models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    goals = db.query(goal_models.Goal).filter(goal_models.Goal.user_id == current_user.id).all()
    return goals

@router.put("/goals/{goal_id}", response_model=goal_schemas.GoalResponse)
async def update_financial_goal(
    goal_id: int,
    goal_update: goal_schemas.GoalUpdate,
    current_user: user_models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    goal = db.query(goal_models.Goal).filter(
        goal_models.Goal.id == goal_id,
        goal_models.Goal.user_id == current_user.id
    ).first()
    if not goal:
        raise HTTPException(status_code=404, detail="Goal not found")
    
    for field, value in goal_update.dict(exclude_unset=True).items():
        setattr(goal, field, value)
    
    db.add(goal)
    db.commit()
    db.refresh(goal)
    return goal

@router.delete("/goals/{goal_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_financial_goal(
    goal_id: int,
    current_user: user_models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    goal = db.query(goal_models.Goal).filter(
        goal_models.Goal.id == goal_id,
        goal_models.Goal.user_id == current_user.id
    ).first()
    if not goal:
        raise HTTPException(status_code=404, detail="Goal not found")
    
    db.delete(goal)
    db.commit()
    return
