
from pathlib import Path
import pandas as pd

# Week 2 project folder
PROJECT_DIR = Path(__file__).resolve().parent

# Original Week 1 dataset (read-only)
DATA_FILE = (
    PROJECT_DIR.parent
    / "Week-1-Strategic-Planning"
    / "data"
    / "DataCoSupplyChainDataset.csv"
)

# Week 2 output folder
OUTPUT_DIR = PROJECT_DIR / "data"
OUTPUT_DIR.mkdir(exist_ok=True)

print("=" * 55)
print("WEEK 2: DATA CLEANING AND PREPROCESSING")
print("=" * 55)

# Load dataset
df = pd.read_csv(DATA_FILE, encoding="latin1", low_memory=False)

print("\n1. ORIGINAL DATA OVERVIEW")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])
print("Duplicate rows:", df.duplicated().sum())

# Missing-value analysis
print("\n2. MISSING VALUES")
missing = df.isnull().sum()
missing = missing[missing > 0].sort_values(ascending=False)

if missing.empty:
    print("No missing values found.")
else:
    print(missing.to_string())

# Data types
print("\n3. DATA TYPES")
print(df.dtypes.value_counts().to_string())

# Remove exact duplicate rows
before = len(df)
df = df.drop_duplicates()
removed = before - len(df)

print("\n4. DUPLICATE CLEANING")
print("Exact duplicate rows removed:", removed)

# Standardize column names for easier analysis
df.columns = (
    df.columns.str.strip()
    .str.lower()
    .str.replace(r"[^a-z0-9]+", "_", regex=True)
    .str.strip("_")
)

# Save missing-value report before filling anything

# Remove columns that are empty or not useful
columns_to_drop = [
    "product_description",
    "order_zipcode"
]

# Remove personal and sensitive customer information
privacy_columns = [
    "customer_email",
    "customer_password",
    "customer_fname",
    "customer_lname",
    "customer_street",
    "customer_zipcode",
    "customer_id",
    "order_customer_id"
]

columns_to_drop.extend(privacy_columns)

# Drop only columns that exist in the dataset
columns_to_drop = [
    col for col in columns_to_drop if col in df.columns
]

df = df.drop(columns=columns_to_drop)

print("\n5. COLUMNS REMOVED")
print(columns_to_drop)

print("\n6. FINAL DATA QUALITY")
print("Final rows:", len(df))
print("Final columns:", len(df.columns))
print("Remaining missing values:", df.isnull().sum().sum())

missing_report = (
    df.isnull().sum()
    .rename("missing_count")
    .to_frame()
)
missing_report["missing_percentage"] = (
    missing_report["missing_count"] / len(df) * 100
).round(2)

missing_report.to_csv(
    OUTPUT_DIR / "missing_values_report.csv"
)

# Save cleaned dataset

# Remove unnecessary and sensitive columns
columns_to_drop = [
    "product_description",
    "order_zipcode",
    "customer_email",
    "customer_password",
    "customer_fname",
    "customer_lname",
    "customer_street",
    "customer_zipcode",
    "customer_id",
    "order_customer_id"
]

# Keep only columns that exist
columns_to_drop = [
    col for col in columns_to_drop if col in df.columns
]

# Remove selected columns
df = df.drop(columns=columns_to_drop)

print("\n5. COLUMNS REMOVED")
print(columns_to_drop)

# Check remaining missing values
print("\n6. REMAINING MISSING VALUES")
print(df.isnull().sum()[df.isnull().sum() > 0])

# Final dataset summary
print("\n7. FINAL CLEANED DATA SUMMARY")
print("Final rows:", df.shape[0])
print("Final columns:", df.shape[1])
print("Duplicate rows:", df.duplicated().sum())
print("Total missing values:", df.isnull().sum().sum())

# Save cleaned dataset
output_file = OUTPUT_DIR / "cleaned_logistics_data.csv"
df.to_csv(output_file, index=False)

print("\nCleaned dataset saved successfully!")
print(output_file)
