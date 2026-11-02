
import pandas as pd

df = pd.read_csv("data/cleaned_logistics_data.csv")

print("TOTAL ROWS:", df.shape[0])
print("TOTAL COLUMNS:", df.shape[1])

print("\nDATA TYPES:")
print(df.dtypes)

print("\nDATE COLUMN CHECK:")

for col in df.columns:
    if "date" in col.lower():
        print(col, ":", df[col].dtype)

print("\nMISSING VALUES:", df.isnull().sum().sum())
