import pandas as pd

# Load the dataset
df = pd.read_csv("../data/invoices.csv")

# Identify mismatched invoices
df["Mismatch"] = df["PO_Amount"] != df["Invoice_Amount"]

# Save mismatches
df[df["Mismatch"]].to_csv("../data/mismatched_invoices.csv", index=False)

print(f"✅ Invoice matching completed. {df['Mismatch'].sum()} anomalies found.")
