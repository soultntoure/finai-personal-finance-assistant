import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.preprocessing import LabelEncoder

from ..data_processing.preprocess import clean_transaction_data, feature_engineer_transactions, load_raw_data

def train_transaction_categorizer(data_path: str = "dummy_transactions.csv", model_output_path: str = "../models/transaction_categorizer.pkl"):
    """Trains a model for transaction categorization."""
    print("Training transaction categorizer...")
    df = load_raw_data(data_path)
    df = clean_transaction_data(df)
    df = feature_engineer_transactions(df)

    # For simplicity, using raw category for training. In real-world, might use user-corrected categories.
    if 'category_raw' not in df.columns:
        print("No 'category_raw' column found for training. Skipping.")
        return

    X = df[['amount', 'day_of_week', 'month', 'is_weekend']] # Example features
    y = df['category_raw']

    # Encode target labels if they are strings
    le = LabelEncoder()
    y_encoded = le.fit_transform(y)

    X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    score = model.score(X_test, y_test)
    print(f"Transaction Categorizer Accuracy: {score:.2f}")

    # Save model and label encoder
    joblib.dump({'model': model, 'label_encoder': le}, model_output_path)
    print(f"Transaction categorizer saved to {model_output_path}")

def train_behavioral_predictor(data_path: str = "dummy_transactions.csv", model_output_path: str = "../models/behavioral_predictor.pkl"):
    """Trains a model to predict future spending behavior (e.g., next month's total spending)."""
    print("Training behavioral predictor...")
    df = load_raw_data(data_path)
    df = clean_transaction_data(df)
    df['month_year'] = df['date'].dt.to_period('M')

    # Aggregate monthly spending per user
    monthly_spending = df.groupby(['user_id', 'month_year'])['amount'].sum().reset_index()
    monthly_spending['next_month_spending'] = monthly_spending.groupby('user_id')['amount'].shift(-1)
    monthly_spending.dropna(inplace=True)

    if monthly_spending.empty:
        print("Not enough data to train behavioral predictor. Skipping.")
        return

    X = monthly_spending[['amount']]
    y = monthly_spending['next_month_spending']

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)

    joblib.dump(model, model_output_path)
    print(f"Behavioral predictor saved to {model_output_path}")

def train_investment_optimizer(data_path: str = "dummy_investment_data.csv", model_output_path: str = "../models/investment_optimizer.pkl"):
    """Trains a model for investment strategy optimization."""
    print("Training investment optimizer... (Placeholder)")
    # This would involve more complex data: user risk tolerance, financial goals, market data.
    # For MVP, this might be a simple rule-based system or a very basic linear model.
    # Dummy model saving
    model = {'message': 'Dummy investment optimizer model'}
    joblib.dump(model, model_output_path)
    print(f"Investment optimizer saved to {model_output_path}")

if __name__ == "__main__":
    # Create a dummy data file for testing
    dummy_data = {
        'transaction_id': [1, 2, 3, 4, 5, 6],
        'amount': [10.5, 25.0, 5.75, 50.0, 15.0, 30.0],
        'date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-02-01', '2023-02-02', '2023-03-01'],
        'name': ['Coffee', 'Groceries', 'Movie', 'Rent', 'Restaurant', 'Electricity'],
        'category_raw': ['Food', 'Household', 'Entertainment', 'Housing', 'Food', 'Utilities'],
        'user_id': [1, 1, 1, 1, 1, 1]
    }
    pd.DataFrame(dummy_data).to_csv("dummy_transactions.csv", index=False)

    train_transaction_categorizer("dummy_transactions.csv")
    train_behavioral_predictor("dummy_transactions.csv")
    train_investment_optimizer()

    import os
    os.remove("dummy_transactions.csv")
