import json
from models import Transaction
import os

DATA_FILE = 'data/transactions.json'

def load_transactions():
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE,'r') as f:
            data = json.load(f)
            return [Transaction(**item) for item in data]
    except json.JSONDecodeError:
        return []

def save_transcation(transactions):
    with open(DATA_FILE,'w') as f:
        json.dump([t.to_dict() for t in transactions],f,indent=4)
