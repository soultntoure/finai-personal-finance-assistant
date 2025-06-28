from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ...core.database import get_db
from ...core.deps import get_current_user
from ...schemas import transaction as transaction_schemas
from ...models import transaction as transaction_models, user as user_models
from ...services.plaid_service import PlaidService

router = APIRouter()

@router.post("/transactions/sync", status_code=status.HTTP_202_ACCEPTED)
async def sync_transactions(
    current_user: user_models.User = Depends(get_current_user),
    plaid_service: PlaidService = Depends()
):
    # In a real app, this would trigger an async task to fetch transactions
    # and process them, potentially with ML categorization.
    # For MVP, a placeholder or direct call if simplified.
    # Example: plaid_service.fetch_and_store_transactions(user_id=current_user.id)
    return {"message": "Transaction sync initiated. Check back later for updates.", "user_id": current_user.id}

@router.get("/transactions", response_model=list[transaction_schemas.TransactionResponse])
async def get_user_transactions(
    current_user: user_models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    transactions = db.query(transaction_models.Transaction).filter(transaction_models.Transaction.user_id == current_user.id).all()
    return transactions

@router.put("/transactions/{transaction_id}", response_model=transaction_schemas.TransactionResponse)
async def update_transaction_category(
    transaction_id: int,
    transaction_update: transaction_schemas.TransactionUpdateCategory,
    current_user: user_models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    transaction = db.query(transaction_models.Transaction).filter(
        transaction_models.Transaction.id == transaction_id,
        transaction_models.Transaction.user_id == current_user.id
    ).first()
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    
    transaction.category = transaction_update.category
    db.add(transaction)
    db.commit()
    db.refresh(transaction)
    return transaction
