import pandas as pd

df = pd.read_csv("data/cleaned_logistics_data.csv")

print("FINAL DATA QUALITY CHECK")
print("=" * 40)

print("Total Rows:", df.shape[0])
print("Total Columns:", df.shape[1])

print("Duplicate Rows:", df.duplicated().sum())

print("Total Missing Values:", df.isnull().sum().sum())

print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes.value_counts())

print("\nFinal Check Completed!")