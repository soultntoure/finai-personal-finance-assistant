import httpx
from typing import Dict, Any

from ..core.config import settings
from ..core.exceptions import FinAIException

class MLClientService:
    def __init__(self):
        self.ml_service_url = settings.BACKEND_ML_SERVICE_URL
        self.client = httpx.AsyncClient(base_url=self.ml_service_url)

    async def get_transaction_category_prediction(self, transaction_text: str) -> Dict[str, Any]:
        try:
            response = await self.client.post(
                "/predict/category",
                json={"transaction_text": transaction_text}
            )
            response.raise_for_status() # Raise HTTPStatusError for bad responses (4xx or 5xx)
            return response.json()
        except httpx.HTTPStatusError as e:
            raise FinAIException(f"ML Service error for category prediction: {e.response.text}", status_code=e.response.status_code)
        except httpx.RequestError as e:
            raise FinAIException(f"Could not connect to ML Service for category prediction: {e}")

    async def get_budget_recommendations(self, user_id: int) -> Dict[str, Any]:
        try:
            response = await self.client.post(
                "/predict/budget",
                json={"user_id": user_id}
            )
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            raise FinAIException(f"ML Service error for budget recommendations: {e.response.text}", status_code=e.response.status_code)
        except httpx.RequestError as e:
            raise FinAIException(f"Could not connect to ML Service for budget recommendations: {e}")

    async def get_investment_recommendations(self, user_id: int) -> Dict[str, Any]:
        try:
            response = await self.client.post(
                "/predict/investment",
                json={"user_id": user_id}
            )
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            raise FinAIException(f"ML Service error for investment recommendations: {e.response.text}", status_code=e.response.status_code)
        except httpx.RequestError as e:
            raise FinAIException(f"Could not connect to ML Service for investment recommendations: {e}")
