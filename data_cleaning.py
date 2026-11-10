"""
Data cleaning for AI Tools Usage Analytics.
Run: python data_cleaning.py
Input: AI_Tools_Usage_Dashboard_Dataset.xlsx
Output: clean_dataset.csv
"""
from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "AI_Tools_Usage_Dashboard_Dataset.xlsx"
OUTPUT_FILE = BASE_DIR / "clean_dataset.csv"

def clean_data():
    if not INPUT_FILE.exists():
        raise FileNotFoundError(f"Dataset not found: {INPUT_FILE}")

    df = pd.read_excel(INPUT_FILE, sheet_name="Dataset")
    print("Original shape:", df.shape)

    # Remove exact duplicate rows and duplicate user IDs.
    df = df.drop_duplicates()
    if "User_ID" in df.columns:
        df = df.drop_duplicates(subset=["User_ID"], keep="first")

    # Convert columns to numeric where appropriate.
    for col in df.columns:
        if col != "User_ID":
            df[col] = pd.to_numeric(df[col], errors="coerce")

    # Fill missing numeric values with the column median.
    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    for col in numeric_cols:
        if df[col].isna().any():
            df[col] = df[col].fillna(df[col].median())

    # Apply sensible validity limits to known fields.
    limits = {
        "Age": (13, 100),
        "Experience_Years": (0, 80),
        "Daily_AI_Usage_Hours": (0, 24),
        "Num_AI_Tools_Used": (0, 100),
        "AI_Queries_Per_Day": (0, 10000),
        "Learning_Hours_Per_Week": (0, 168),
        "Monthly_Subscription_Cost_USD": (0, 100000),
        "Productivity_Rating": (0, 10),
        "Satisfaction_Score": (0, 10),
        "Trust_Score": (0, 10),
        "Time_Saved_Hours_Per_Week": (0, 168),
    }
    for col, (low, high) in limits.items():
        if col in df.columns:
            df = df[df[col].between(low, high)]

    df = df.sort_values("User_ID").reset_index(drop=True)
    df.to_csv(OUTPUT_FILE, index=False)

    print("Cleaned shape:", df.shape)
    print("Saved cleaned dataset to:", OUTPUT_FILE.name)
    print("Missing values remaining:", int(df.isna().sum().sum()))
    print("Duplicate rows remaining:", int(df.duplicated().sum()))
    return df

if __name__ == "__main__":
    clean_data()
