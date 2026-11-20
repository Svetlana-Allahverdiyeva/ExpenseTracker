import json
import os
#DATA_FILE = "data/expenses.json"


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "data", "expenses.json")

def loadExpenses():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            expenses = json.load(file)

        return expenses
    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        return []

def saveExpenses(expenses):
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    
    with open (DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(expenses, file, indent=4, ensure_ascii=False)