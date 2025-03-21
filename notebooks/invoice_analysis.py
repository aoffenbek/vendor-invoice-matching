import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load datasets
df = pd.read_csv("../data/invoices.csv")
mismatches = pd.read_csv("../data/mismatched_invoices.csv")

# Count anomaly types
anomaly_counts = mismatches["Mismatch_Type"].value_counts()

# Bar plot of anomaly types
plt.figure(figsize=(6,4))
sns.barplot(x=anomaly_counts.index, y=anomaly_counts.values, palette="coolwarm")
plt.title("Invoice Anomaly Types")
plt.xlabel("Mismatch Type")
plt.ylabel("Count")
plt.show()
