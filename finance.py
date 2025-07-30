from models import Transaction
from exporter import CSVExporter
from storage import save_transcation,load_transactions
from utils import display_transactions , display_summary , display_transactions_for_month , display_summary_for_month

def main():
    print("\nWelcome to Personal Finance CLI Assistant\n")
    transactions = load_transactions()

    while True:
        print("1. Add Transaction")
        print("2. Update Transaction")
        print("3. Delete Transaction")
        print("4. View Transactions (all)")
        print("5. View Summary (all)")
        print("6. View Transactions (month-wise)")
        print("7. View Summary (month-wise)")
        print("8. Export to CSV")
        print("9. Exit")

        choice = input("\nWhat do you want to do today? (1-9):")

        if choice == '1':
            txn = Transaction.from_input()
            transactions.append(txn)
            save_transcation(transactions)
            print("\nTransaction added!\n")

        elif choice == '2':
            display_transactions(transactions)

            if len(transactions) == 0:
                print("No transactions to update\n")
                continue

            index = int(input("Which transaction do you want to modify?\nEnter the number:"))
            index -= 1

            if 0 <= index < len(transactions):
                transactions[index].update()
                save_transcation(transactions)
                print("\nTransaction updated.\n")
            else:
                print("Invalid index.\n")

        elif choice == '3':
            display_transactions(transactions)

            if len(transactions) == 0:
                print("No transactions to delete\n")
                continue

            try:
                index = int(input("Which transaction do you want to delete?\nEnter the number:"))
                index -= 1

                if 0 <= index < len(transactions):
                    confirm = input("To proceed , enter 'YES'\n".strip().lower())

                    if confirm == 'yes':
                        deleted_transaction = transactions.pop(index)
                        save_transcation(transactions)
                        print(f"\nTransaction deleted : {deleted_transaction.desc} (${deleted_transaction.amount})\n")
                    else:
                        print("Delete cancelled.\n")
            except ValueError:
                print("Invalid index.\n")

        elif choice == '4':
            display_transactions(transactions)

        elif choice == '5':
            display_summary(transactions)

        elif choice == '6':
            month = input("Enter the month (YYYY-MM):".strip())
            display_transactions_for_month(transactions,month)

        elif choice == '7':
            month = input("Enter the month (YYYY-MM):".strip())
            display_summary_for_month(transactions, month)

        elif choice == '8':
            print("Export Options:")
            print("1. Export All")
            print("2. Export by Date Range")
            print("3. Export by Type (income/expense)")
            print("4. Export by Type and Date Range")

            export_choice = input("What do you want to do?")

            exporter = CSVExporter(transactions)

            if export_choice == '1':
                exporter.export(filter_type='all')
            elif export_choice == '2':
                start_date = input("Enter start date (YYYY-MM-DD):")
                end_date = input("Enter end date (YYYY-MM-DD):")
                exporter.export(filter_type='date_range',start_date=start_date,end_date=end_date)
            elif export_choice == '3':
                txn_type = input("Enter transaction type (income/expense):")
                exporter.export(filter_type='type',txn_type=txn_type)
            elif export_choice == '4':
                start_date = input("Enter start date (YYYY-MM-DD):")
                end_date = input("Enter end date (YYYY-MM-DD):")
                txn_type = input("Enter transaction type (income/expense):")
                exporter.export(filter_type='date_and_type',start_date=start_date,end_date=end_date,txn_type=txn_type)
            else:
                print("Invalid export option.\n")

        elif choice == '9':
            print("Have a good day!")
            break

        else:
            print("\nInvalid option selected. Try again!\n")

if __name__ == '__main__':
    main()