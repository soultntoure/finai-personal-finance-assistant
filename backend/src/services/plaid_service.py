import plaid
from plaid.model.link_token_create_request import LinkTokenCreateRequest
from plaid.model.link_token_create_request_user import LinkTokenCreateRequestUser
from plaid.model.products import Products
from plaid.model.country_code import CountryCode
from plaid.model.item_public_token_exchange_request import ItemPublicTokenExchangeRequest
from plaid.model.transactions_sync_request import TransactionsSyncRequest

from sqlalchemy.orm import Session

from ..core.config import settings
from ..models import user as user_models, transaction as transaction_models
from ..core.exceptions import PlaidAPIException

class PlaidService:
    def __init__(self):
        self.client_id = settings.BACKEND_PLAID_CLIENT_ID
        self.secret = settings.BACKEND_PLAID_SECRET
        self.env = settings.BACKEND_PLAID_ENV
        
        environment = getattr(plaid.Environment, self.env.upper())
        configuration = plaid.Configuration(
            host=environment,
            api_key={
                'clientId': self.client_id,
                'secret': self.secret,
            }
        )
        self.api_client = plaid.ApiClient(configuration)
        self.client = plaid.PlaidApi(self.api_client)

    async def create_link_token(self, user_id: int, user_email: str) -> str:
        request = LinkTokenCreateRequest(
            products=[Products('transactions')],
            client_name="FinAI",
            country_codes=[CountryCode('US')],
            language='en',
            user=LinkTokenCreateRequestUser(client_user_id=str(user_id)),
            redirect_uri='http://localhost:3000/plaid-redirect' # For OAuth flows
        )
        try:
            response = self.client.link_token_create(request)
            return response.link_token
        except plaid.ApiException as e:
            raise PlaidAPIException(detail=f"Failed to create link token: {e.body}")

    async def exchange_public_token(self, public_token: str) -> str:
        request = ItemPublicTokenExchangeRequest(public_token=public_token)
        try:
            response = self.client.item_public_token_exchange(request)
            return response.access_token
        except plaid.ApiException as e:
            raise PlaidAPIException(detail=f"Failed to exchange public token: {e.body}")

    async def fetch_and_store_transactions(self, db: Session, user_id: int, access_token: str):
        # This would ideally be an async Celery task
        try:
            request = TransactionsSyncRequest(
                access_token=access_token,
                count=100, # Max number of transactions to return
            )
            response = self.client.transactions_sync(request)
            transactions = response.added
            
            for t in transactions:
                # Basic categorization for MVP, ML service will enhance this
                category = t.personal_finance_category.primary if t.personal_finance_category else 'Uncategorized'
                new_transaction = transaction_models.Transaction(
                    user_id=user_id,
                    plaid_transaction_id=t.transaction_id,
                    account_id=t.account_id,
                    name=t.name,
                    amount=t.amount,
                    currency='USD', # Assuming USD for MVP
                    date=t.date,
                    category=category,
                    transaction_type='debit' if t.amount > 0 else 'credit' # Simplified
                )
                db.add(new_transaction)
            db.commit()
        except plaid.ApiException as e:
            db.rollback()
            raise PlaidAPIException(detail=f"Failed to fetch and store transactions: {e.body}")
