import pandas as pd
import numpy as np

def clean_transaction_data(df: pd.DataFrame) -> pd.DataFrame:
    """Cleans raw transaction data. Example operations: handle missing values, standardize formats."""
    df = df.copy()
    df['amount'] = pd.to_numeric(df['amount'], errors='coerce')
    df.dropna(subset=['amount', 'date'], inplace=True)
    df['date'] = pd.to_datetime(df['date'])
    # Basic text cleaning for transaction names
    df['name'] = df['name'].str.lower().str.strip()
    return df

def feature_engineer_transactions(df: pd.DataFrame) -> pd.DataFrame:
    """Extracts features for ML models from transaction data."""
    df = df.copy()
    df['day_of_week'] = df['date'].dt.dayofweek
    df['month'] = df['date'].dt.month
    df['year'] = df['date'].dt.year
    df['is_weekend'] = df['day_of_week'].isin([5, 6]).astype(int)
    # Add more complex features like average spending per merchant, time between transactions etc.
    return df

def load_raw_data(file_path: str) -> pd.DataFrame:
    """Simulates loading raw data for processing."""
    # In a real scenario, this would load from S3 or a data warehouse
    print(f"Loading data from {file_path}")
    # Example: return pd.read_csv(file_path)
    return pd.DataFrame({
        'transaction_id': [1, 2, 3],
        'amount': [10.5, 25.0, 5.75],
        'date': ['2023-01-01', '2023-01-02', '2023-01-03'],
        'name': ['Coffee Shop', 'Supermarket', 'Online Purchase'],
        'category_raw': ['Food & Drink', 'Groceries', 'Shopping'],
        'user_id': [1, 1, 1]
    })

if __name__ == "__main__":
    print("Running data preprocessing example...")
    raw_df = load_raw_data("dummy_transactions.csv")
    cleaned_df = clean_transaction_data(raw_df)
    features_df = feature_engineer_transactions(cleaned_df)
    print("Cleaned and engineered features:")
    print(features_df.head())
