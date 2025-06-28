from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import os
import pandas as pd

class TransactionText(BaseModel):
    transaction_text: str

class UserId(BaseModel):
    user_id: int

app = FastAPI(
    title="FinAI ML Service",
    description="API for FinAI's machine learning models."
)

# Load models on startup
models = {}

@app.on_event("startup")
async def load_models():
    global models
    model_dir = "./src/models"
    try:
        models['categorizer'] = joblib.load(os.path.join(model_dir, "transaction_categorizer.pkl"))
        models['behavioral_predictor'] = joblib.load(os.path.join(model_dir, "behavioral_predictor.pkl"))
        models['investment_optimizer'] = joblib.load(os.path.join(model_dir, "investment_optimizer.pkl"))
        print("ML models loaded successfully.")
    except FileNotFoundError as e:
        print(f"Error loading ML models: {e}. Ensure models are trained and present in {model_dir}/")
        # For production, you might raise an error or have a fallback mechanism.
    except Exception as e:
        print(f"Unexpected error loading ML models: {e}")

@app.post("/predict/category")
async def predict_category(data: TransactionText):
    if 'categorizer' not in models:
        raise HTTPException(status_code=500, detail="Transaction categorizer model not loaded.")
    
    # Dummy feature extraction for demo
    # In a real scenario, this needs to match features used during training
    input_df = pd.DataFrame([[0.0, 0, 0, 0]], columns=['amount', 'day_of_week', 'month', 'is_weekend'])
    
    model_components = models['categorizer']
    model = model_components['model']
    le = model_components['label_encoder']

    prediction_encoded = model.predict(input_df)[0]
    predicted_category = le.inverse_transform([prediction_encoded])[0]

    return {"transaction_text": data.transaction_text, "predicted_category": predicted_category}

@app.post("/predict/budget")
async def predict_budget_recommendations(data: UserId):
    if 'behavioral_predictor' not in models:
        raise HTTPException(status_code=500, detail="Behavioral predictor model not loaded.")
    
    # Placeholder: In reality, fetch user's financial history from DB via backend
    # and pass relevant features to the model.
    # For now, a dummy prediction based on user_id.
    
    # Example: predict future spending based on past spending for this user.
    # This is a very simplified example. Real models would need more context.
    dummy_past_spending = 1000.0 if data.user_id == 1 else 800.0
    predicted_next_month_spending = models['behavioral_predictor'].predict([[dummy_past_spending]])[0]

    # Convert spending prediction into budget recommendations per category
    # This part would involve more business logic and potentially another model.
    category_recommendations = {
        "Groceries": round(predicted_next_month_spending * 0.3, 2),
        "Transport": round(predicted_next_month_spending * 0.15, 2),
        "Entertainment": round(predicted_next_month_spending * 0.1, 2),
        "Utilities": round(predicted_next_month_spending * 0.2, 2),
        "Miscellaneous": round(predicted_next_month_spending * 0.25, 2)
    }
    
    return {
        "category_recommendations": category_recommendations,
        "overall_savings_target": round(predicted_next_month_spending * 0.1, 2), # 10% target
        "explanation": f"Budget recommendations based on your predicted future spending of ${predicted_next_month_spending:.2f} and an overall 10% savings target."
    }

@app.post("/predict/investment")
async def predict_investment_recommendations(data: UserId):
    if 'investment_optimizer' not in models:
        raise HTTPException(status_code=500, detail="Investment optimizer model not loaded.")
    
    # Placeholder: Real-world model would take user risk, goals, current portfolio.
    # The dummy model just returns a static recommendation.
    dummy_recommendation = models['investment_optimizer']['message'] if isinstance(models['investment_optimizer'], dict) else "Generic Investment Advice"
    
    return {
        "strategy_type": "Balanced Growth (AI-Optimized)",
        "suggested_allocations": {"Stocks": 0.65, "Bonds": 0.25, "Cash": 0.10},
        "projected_returns": 0.08,
        "risk_level": "Medium-High",
        "explanation": f"AI-driven strategy: {dummy_recommendation}. Focuses on long-term capital appreciation with moderate risk."
    }

@app.get("/health")
async def health_check():
    return {"status": "ok", "message": "ML Service is running and models loaded: " + str(list(models.keys()))}
