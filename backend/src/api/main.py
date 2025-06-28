from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from ..core.config import settings

from .v1 import auth, users, transactions, budgeting, savings, investments, goals

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Set up CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS], # Or use ["*"] for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Include API routers
app.include_router(auth.router, prefix=settings.API_V1_STR, tags=["Auth"])
app.include_router(users.router, prefix=settings.API_V1_STR + "/users", tags=["Users"])
app.include_router(transactions.router, prefix=settings.API_V1_STR, tags=["Transactions"])
app.include_router(budgeting.router, prefix=settings.API_V1_STR, tags=["Budgets"])
app.include_router(savings.router, prefix=settings.API_V1_STR, tags=["Savings"])
app.include_router(investments.router, prefix=settings.API_V1_STR, tags=["Investments"])
app.include_router(goals.router, prefix=settings.API_V1_STR, tags=["Goals"])

@app.get(settings.API_V1_STR + "/health")
async def health_check():
    return {"status": "ok", "message": "FinAI Backend is running"}
