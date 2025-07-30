# Personal Finance CLI

A simple and extensible command-line tool to:
  1. manage your personal finances
  2. track income/expenses
  3. export reports

---
## Features:
- Add new income or expense transaction
- Update existing transaction (description , amount, type and date)
- Delete transactions
- View transactions sorted by date (newest first)
- View transactions for a specific month
- View summary (complete or for a specific month)
- Export data to CSV with flexible filters:
  - Export all
  - Export by date range
  - Export by transaction type
  - Export by transaction type and date range
- Dynamic CSV filenames (based on the filter and timestamp)
- Dedicated folder to save the exported CSVs
- Transactions are also saved in JSON format (data/transactions.json)
---

## Project Structure
personal-finance-cli/
├── finance.py # Main CLI interface
├── exporter.py # CSV export logic and filtering
├── utils.py # Helper functions (display formatting, date/month filters)
├── models.py # (Not included here, expected to define the Transaction class)
├── storage.py # (Not included here, expected to handle JSON persistence)
├── data/
│ └── transactions.json # Local transaction store
├── csv/ # Exported CSV files
└── README.md # Project documentation

## Getting Started
### Prerequisities
- Python 3.7 or later

### Setup 
1. Clone the repository or copy the files into a folder
   ```bash
   git clone https://github.com/TejasviR1412/Expense-Tracker-CLI.git
   cd personal-finance-cli
   ```
   
3. Create required folders:
   ```
   mkdir -p data csv
   touch data/transactions.json
   ```
   
5. Run the app:
   python finance.py
