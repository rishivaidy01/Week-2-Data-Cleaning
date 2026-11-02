import pandas as pd

# Load cleaned dataset
df = pd.read_csv("data/cleaned_logistics_data.csv")

# Numerical columns for outlier analysis
columns = [
    "sales",
    "order_profit_per_order",
    "days_for_shipping_real",
    "order_item_quantity",
    "product_price"
]

print("OUTLIER ANALYSIS REPORT")
print("=" * 50)

outlier_results = []

for col in columns:

    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)

    IQR = Q3 - Q1

    lower_limit = Q1 - 1.5 * IQR
    upper_limit = Q3 + 1.5 * IQR

    outliers = df[
        (df[col] < lower_limit) |
        (df[col] > upper_limit)
    ]

    outlier_results.append({
        "Column": col,
        "Lower Limit": lower_limit,
        "Upper Limit": upper_limit,
        "Outlier Count": len(outliers)
    })

    print("\nColumn:", col)
    print("Lower Limit:", round(lower_limit, 2))
    print("Upper Limit:", round(upper_limit, 2))
    print("Outliers:", len(outliers))

# Save report
report = pd.DataFrame(outlier_results)

report.to_csv(
    "reports/outlier_analysis_report.csv",
    index=False
)

print("\nOutlier report saved successfully!")