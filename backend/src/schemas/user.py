from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True # Pydantic v2: from_orm = True for v1

class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    # Add other updatable fields as needed
