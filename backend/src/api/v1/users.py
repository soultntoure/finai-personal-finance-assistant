from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ...core.database import get_db
from ...core.deps import get_current_user
from ...schemas import user as user_schemas
from ...models import user as user_models

router = APIRouter()

@router.get("/me", response_model=user_schemas.UserResponse)
async def read_current_user(
    current_user: user_models.User = Depends(get_current_user)
):
    return current_user

@router.put("/me", response_model=user_schemas.UserResponse)
async def update_current_user(
    user_update: user_schemas.UserUpdate,
    current_user: user_models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    # Example: Update email if provided
    if user_update.email and user_update.email != current_user.email:
        existing_user = db.query(user_models.User).filter(user_models.User.email == user_update.email).first()
        if existing_user:
            raise HTTPException(status_code=400, detail="Email already taken")
        current_user.email = user_update.email
    
    # Example: Update other fields, e.g., name, if added to schema/model

    db.add(current_user)
    db.commit()
    db.refresh(current_user)
    return current_user
