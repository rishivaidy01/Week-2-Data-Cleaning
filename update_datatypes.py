
import pandas as pd

# Load cleaned dataset
file_path = "data/cleaned_logistics_data.csv"
df = pd.read_csv(file_path)

print("BEFORE DATE CONVERSION")
print(df[[
    "order_date_dateorders",
    "shipping_date_dateorders"
]].dtypes)

# Convert date columns
date_columns = [
    "order_date_dateorders",
    "shipping_date_dateorders"
]

for col in date_columns:
    df[col] = pd.to_datetime(
        df[col],
        errors="coerce"
    )

# Check conversion results
print("\nAFTER DATE CONVERSION")

for col in date_columns:
    print("\nColumn:", col)
    print("Data type:", df[col].dtype)
    print("Invalid dates:", df[col].isna().sum())

# Save updated dataset
df.to_csv(file_path, index=False)

print("\nUpdated dataset saved successfully!")
print("Total rows:", df.shape[0])
print("Total columns:", df.shape[1])
