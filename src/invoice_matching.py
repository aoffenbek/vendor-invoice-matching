import pandas as pd

# Load the dataset
df = pd.read_csv("../data/invoices.csv")

# Set a tolerance threshold (5% difference is allowed)
TOLERANCE = 0.05

# Compute absolute percentage difference
df["Diff_Percentage"] = abs(df["Invoice_Amount"] - df["PO_Amount"]) / df["PO_Amount"]

# Identify mismatches based on tolerance
df["Mismatch"] = df["Diff_Percentage"] > TOLERANCE

# Categorize anomaly types
def categorize_mismatch(row):
    if row["Invoice_Amount"] > row["PO_Amount"]:
        return "Overcharged"
    elif row["Invoice_Amount"] < row["PO_Amount"]:
        return "Undercharged"
    return "Match"

df["Mismatch_Type"] = df.apply(categorize_mismatch, axis=1)

# Save mismatches
mismatches = df[df["Mismatch"]]
mismatches.to_csv("../data/mismatched_invoices.csv", index=False)

print(f"✅ Invoice matching completed. {len(mismatches)} anomalies found.")
