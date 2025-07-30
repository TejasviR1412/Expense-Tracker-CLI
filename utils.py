from datetime import datetime

def display_transactions(transactions):
    """
        Function to display all the transactions
    """

    if not transactions:
        print("\nNo transactions to display.\n")
        return

    #sort the transactions in descending order of the date
    sorted_transactions = sorted(transactions,key=lambda t: datetime.strptime(t.date,'%Y-%m-%d'),reverse=True)

    print("\nTransactions (Newest First):")
    print("--------------------------------------------------------------------------")
    print(f"# . DATE       | TRANSACTION TYPE | AMOUNT    | CATEGORY   | DESCRIPTION")
    print("--------------------------------------------------------------------------")

    for i,t in enumerate(sorted_transactions):
        print(f"{i+1} . {t.date} | {t.txn_type.upper():16} | ${t.amount:8.2f} | {t.category:10} | {t.desc}")
        print("--------------------------------------------------------------------------")

def display_summary(transactions):
    """
        Function to total summary
    """

    income = sum(t.amount for t in transactions if t.txn_type=='income')
    expense = sum(t.amount for t in transactions if t.txn_type=='expense')
    balance = income - expense

    print("\n Transaction Summary:")
    print("------------------------------------")
    print(f"Total income: ${income:.2f}")
    print(f"Total expense: ${expense:.2f}")
    print(f"Net Balance: ${balance:.2f}\n")

def display_summary_for_month(transactions, month):
    """
        Function to month-wise summary
    """
    filtered = [t for t in transactions if t.date.startswith(month)]

    if not filtered:
        print("No transactions found for the month:",month)
        return

    income = sum(t.amount for t in filtered if t.txn_type == 'income')
    expense = sum(t.amount for t in filtered if t.txn_type == 'expense')
    balance = income - expense

    print("\n Transaction Summary for:",month)
    print("------------------------------------")
    print(f"Total income: ${income:.2f}")
    print(f"Total expense: ${expense:.2f}")
    print(f"Net Balance: ${balance:.2f}\n")

def display_transactions_for_month(transactions, month):
    """
        Function to month-wise transactions
    """
    filtered = [t for t in transactions if t.date.startswith(month)]

    if not filtered:
        print("No transactions found for the month:", month)
        return

    # sort the transactions in descending order of the date
    sorted_transactions = sorted(filtered, key=lambda t: datetime.strptime(t.date, '%Y-%m-%d'), reverse=True)

    print(f"\nTransactions for {month}(Newest First):")
    print("--------------------------------------------------------------------------")
    print(f"# . DATE       | TRANSACTION TYPE | AMOUNT    | CATEGORY   | DESCRIPTION")
    print("--------------------------------------------------------------------------")

    for i, t in enumerate(sorted_transactions):
        print(f"{i + 1} . {t.date} | {t.txn_type.upper():16} | ${t.amount:8.2f} | {t.category:10} | {t.desc}")
        print("--------------------------------------------------------------------------")