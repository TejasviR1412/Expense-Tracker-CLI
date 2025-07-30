from datetime import datetime

class Transaction:
    def __init__(self, date , amount , category, txn_type,desc):
        self.date = date
        self.amount = amount
        self.category = category
        self.txn_type = txn_type
        self.desc = desc

    def to_dict(self):
        """
            Function returns a dict
        """
        return {
            "date":self.date,
            "amount":self.amount,
            "category":self.category,
            "txn_type":self.txn_type,
            "desc":self.desc
        }

    @classmethod
    def from_input(cls):
        txn_type = input("Enter transaction type (income/expense):").strip().lower()
        amount = float(input("Enter amount:"))
        category = input("Enter category:").strip()
        description = input("Enter description:").strip()
        date = input("Enter date (YYYY-MM-DD):").strip()

        try:
            datetime.strptime(date,'%Y-%m-%d')
        except ValueError:
            print("Invalid date format. Using today's date.\n")
            date = datetime.today().strftime('%Y-%m-%d')

        return cls(date,amount,category,txn_type,description)

    def update(self):
        """
            Function to update a transaction record
        """
        print("\nWhich field do you want to update?")
        print("1. Amount")
        print("2. Type (income/expense)")
        print("3. Description")
        print("4. Category")
        print("5. Cancel")
        print("NOTE : You cannot modify the date!\n")

        selection = input("Enter your choice:").strip()

        if selection == '1':
            print(f"Current Amount: {self.amount}")
            new_amount = float(input("Enter new amount:").strip())

            try:
                self.amount = new_amount
                print("Amount updated.\n")
            except ValueError:
                print("Invalid input. Amount not updated.\n")

        elif selection == '2':
            print(f"Current type: {self.txn_type}")
            new_txn_type = input("Enter new transaction type:".strip()).lower()

            if new_txn_type in ('expense','income'):
                self.txn_type = new_txn_type
                print("Transaction type updated.\n")
            else:
                print("Invalid transaction type. Type not updated.\n")

        elif selection == '3':
            print(f"Current description: {self.desc}")
            new_desc = input("Enter new description".strip())

            if new_desc:
                self.desc = new_desc
                print("Description updated.\n")
            else:
                print("Description cannot be changed.\n")

        elif selection == '4':
            print(f"Current category: {self.category}")
            new_category = input("Enter new category:".strip())

            if new_category:
                self.category = new_category
                print("Category updated.\n")
            else:
                print("Category cannot be changed.\n")

        elif selection == '5':
            print("Update cancelled.\n")

        else:
            print("Invalid option.\n")