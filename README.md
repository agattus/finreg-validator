# FinReg-Validator: Regulatory Data Integrity Engine

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Active-success)](https://github.com/agattus/finreg-validator)

**FinReg-Validator** is an open-source Python library designed to assist financial institutions in automating data quality checks for **CCAR (Comprehensive Capital Analysis and Review)** and **Basel III** regulatory submissions.

In the high-stakes environment of Tier-1 banking, data anomalies—such as null ISINs, future-dated trades, or negative notional values—can lead to failed Federal Stress Tests and significant regulatory fines. This tool acts as a **pre-submission firewall**, ensuring that trading datasets comply with standard Federal Reserve schemas before entering the reporting pipeline.

---

## 🚀 Key Features

### 1. Regulatory Compliance Automation
* **CCAR Readiness:** Validates critical fields required for capital planning and stress testing models.
* **Basel III Alignment:** Enforces non-negative value logic for risk-weighted asset calculations.

### 2. Temporal Logic & TWD (Trade Working Day)
* **Future-Date Protection:** Automatically detects and rejects trades with timestamps beyond the current `datetime`, preventing "Future Dated" anomalies that trigger audit flags.
* **TWD Enforcement:** Ensures trade dates align with valid banking calendars.

### 3. Critical Identifier Validation
* **ISIN & CUSIP Integrity:** Scans millions of rows to ensure no financial instrument lacks a valid regulatory identifier.
* **Null-Value Quarantine:** Segregates records with missing `TradeID` or `NotionalAmount` for manual remediation.

---

## 🛠 Installation

You can clone this repository directly to integrate into your financial ETL pipeline:



## 💻 Usage Example

This library is designed to be dropped into existing Python-based Risk ETL workflows.

```python
from validator import FinRegValidator

# Initialize the validator with your raw trading data
v = FinRegValidator('daily_trades_batch_01.csv')

# Run the full suite of regulatory checks
report = v.check_integrity()

# Output the compliance report
print(report)

# Example Output:
# "RISK FAIL: Found 5 negative values in NotionalAmount."
# "COMPLIANCE FAIL: Found 12 trades with future dates."
