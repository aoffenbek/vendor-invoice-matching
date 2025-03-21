import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Set random seed for reproducibility
random.seed(42)
np.random.seed(42)

# Generate random vendor names
vendors = ["Vendor A", "Vendor B", "Vendor C", "Vendor D", "Vendor E"]

# Create an empty list to store invoice data
invoice_data = []

for i in range(500):  # Generate 500 invoices
    invoice_id = f"INV{1000 + i}"
    po_id = f"PO{2000 + random.randint(0, 100)}"  # Some POs repeat
    vendor = random.choice(vendors)
    invoice_date = datetime(2024, 1, 1) + timedelta(days=random.randint(0, 60))
    po_amount = round(random.uniform(100, 5000), 2)
    invoice_amount = po_amount

    # Introduce anomalies (10% of cases)
    if random.random() < 0.1:
        invoice_amount *= round(random.uniform(0.8, 1.2), 2)  # Slight variation

    invoice_data.append([invoice_id, po_id, vendor, invoice_date.strftime("%Y-%m-%d"), po_amount, invoice_amount])

# Create a DataFrame
df = pd.DataFrame(invoice_data, columns=["InvoiceID", "POID", "Vendor", "InvoiceDate", "PO_Amount", "Invoice_Amount"])

# Save as CSV in the 'data' folder
df.to_csv("../data/invoices.csv", index=False)

print("✅ Dataset generated: data/invoices.csv")
