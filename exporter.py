import csv
import os
from datetime import datetime

class CSVExporter:
    def __init__(self,transactions):
        self.transactions = transactions
        self.output_dir = "csv"
        os.makedirs(self.output_dir,exist_ok=True)

    def _generate_filename(self,label):
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f"{label}_transactions_{timestamp}.csv"
        return os.path.join(self.output_dir,filename)

    def _sort_by_date_desc(self,transactions):
        return sorted(transactions,
                      key=lambda t:datetime.strptime(t.date,'%Y-%m-%d'),
                      reverse=True)

    def export(self,filter_type='all',start_date=None,end_date=None,txn_type=None):
        label = 'all'
        filtered = self.transactions

        if filter_type == 'date_range':
            if not (start_date and end_date):
                print("Start date and End date must be provided.\n")
                return

            label = f"daterange_{start_date}_to_{end_date}"
            filtered = [t for t in self.transactions if start_date <= t.date <= end_date]

        elif filter_type == 'type':
            if txn_type not in ['income','expense']:
                print("Invalid transaction type.\n")
                return

            label = txn_type
            filtered = [t for t in self.transactions if t.txn_type == txn_type]

        elif filter_type == 'date_and_type':
            if not (start_date and end_date):
                print("Start date and End date must be provided.\n")
                return

            if txn_type not in ['income','expense']:
                print("Invalid transaction type.\n")
                return

            label = f"{txn_type}_and_daterange_{start_date}_to_{end_date}"
            filtered = [t for t in self.transactions if (t.txn_type == txn_type) and (start_date <= t.date <= end_date)]

        elif filter_type != 'all':
            print('Invalid filter type.\n')
            return

        if not filtered:
            print("No transactions match the filter.\n")
            return

        sorted_txns = self._sort_by_date_desc(filtered)
        filename = self._generate_filename(label)

        with open(filename,mode='w',encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Date','Transaction Type','Amount','Category','Description'])

            for t in sorted_txns:
                writer.writerow([t.date,t.txn_type,t.amount,t.category,t.desc])

        print(f"{len(filtered)} transactions exported to {filename}")
