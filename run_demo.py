import pandas as pd
from validator import FinRegValidator
import os

# --- Step 1: Generate "Dirty" Banking Data ---
# We are creating a dummy CSV file with intentional regulatory errors
data = {
    'TradeID': ['TRD-2024-001', 'TRD-2024-002', 'TRD-2024-003', 'TRD-2024-004'],
    'ISIN': ['US0378331005', None, 'US5949181045', 'US0378331005'],  # Row 2 has MISSING ISIN
    'NotionalAmount': [1500000, 500000, -10000, 2000000],              # Row 3 has NEGATIVE Amount (Basel III Fail)
    'TradeDate': ['2024-01-15', '2024-01-15', '2024-01-15', '2099-12-31'] # Row 4 has FUTURE Date (CCAR Fail)
}

# Create the CSV file
df = pd.DataFrame(data)
csv_filename = 'regulatory_batch_sample.csv'
df.to_csv(csv_filename, index=False)

print(f"✅ Generated sample batch file: {csv_filename}")
print("-" * 60)
print("🚀 STARTING FinReg-Validator Engine...")
print("-" * 60)

# --- Step 2: Run the Validator ---
# Initialize the engine
v = FinRegValidator(csv_filename)

# Run Integrity Checks
report = v.check_integrity()

# --- Step 3: Print the Report ---
print("\n📄 [CCAR/BASEL III VALIDATION REPORT]")
print("=" * 60)
print(report)
print("=" * 60)
print("\n❌ Process Terminated: Regulatory anomalies detected.")

# Cleanup (Optional: deletes the dummy file after running)
# os.remove(csv_filename)