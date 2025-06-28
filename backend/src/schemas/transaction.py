from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class TransactionBase(BaseModel):
    plaid_transaction_id: Optional[str] = None
    account_id: str
    name: str
    amount: float
    currency: str = "USD"
    date: datetime
    category: Optional[str] = None
    transaction_type: str

class TransactionCreate(TransactionBase):
    pass

class TransactionUpdateCategory(BaseModel):
    category: str = Field(..., example="Groceries")

class TransactionResponse(TransactionBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
