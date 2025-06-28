from sqlalchemy.orm import Session
from typing import Dict, Any

from ..core.database import get_db
from ..models import transaction as transaction_models, user as user_models
from ..schemas import savings as savings_schemas

class FinancialRulesEngine:
    def __init__(self, db: Session = None):
        # In a real app, this might be injected or get its own session context
        self.db = db if db else next(get_db())

    async def get_savings_suggestion(self, user_id: int) -> savings_schemas.SavingsSuggestion:
        # Placeholder for complex business logic based on user data
        # In reality, this would fetch user's income, expenses, existing savings,
        # and apply predefined rules or ML insights to suggest a savings amount.

        # Example: Simple rule - suggest 10% of last month's income if available
        # Or, suggest saving remaining budget if user has a budget setup.

        user_transactions = self.db.query(transaction_models.Transaction).filter(transaction_models.Transaction.user_id == user_id).all()
        
        total_income = sum(t.amount for t in user_transactions if t.transaction_type == 'credit')
        total_expenses = sum(t.amount for t in user_transactions if t.transaction_type == 'debit')

        disposable_income = total_income - total_expenses
        suggested_amount = max(0, disposable_income * 0.10) # 10% of disposable income

        return savings_schemas.SavingsSuggestion(
            suggested_amount=round(suggested_amount, 2),
            reason="Based on 10% of your recent disposable income."
        )

    async def apply_budget_rules(self, user_id: int, budget_data: Dict[str, Any]) -> Dict[str, Any]:
        # Placeholder for applying rules to budget. E.g., warn if budget category is overspent.
        return budget_data
