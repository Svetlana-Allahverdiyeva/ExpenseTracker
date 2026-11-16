from expenses import *
from validation import CATEGORIES
from reports import *

def showMenu():
    print("=" * 40)
    print("     EXPENSE TRACKER     ")
    print("=" * 40)
    print()

    print("""
    1. Add Expense
    2. Show All Expenses
    3. Edit Expense
    4. Delete Expense
    5. Search Expenses
    6. Show Total Expenses
    7. Show Categories
    8. Export to CSV

    0. Exit
    
    """)
    print("=" * 40)

    def startApp():
        while True:
            showMenu()

            choice = int(input("enter choice:"))
            try:
                if choice == "1":
                    title = input("Enter expense title: ")
                    amount = input("Enter expense amount: ")
                    category = input("Enter expense category: ")
                    
                    expense = addExpense(title, amount, category)
                    print("Expense added successfully!")
                    print("Expense ID:", expense["id"])
                
                
                elif choice == "2":
                    expenses = getAllExpenses()
                    if not expenses:
                        print("No expenses found!")
                else:
                    for expense in expenses:
                        print("-" * 40)
                        print("ID:", expense["id"])
                        print("Title:", expense["title"])
                        print("Amount:", expense["amount"])
                        print("Category:", expense["category"])
                        print("Date:", expense["date"])
                
                
                elif choice == "3":
                expenseID = input("Enter expense ID: ")
                title = input("Enter new title: ")
                amount = input("Enter new amount: ")
                category = input("Enter new category: ")
                updateExpense(expenseID, title, amount, category)
                print("Expense updated successfully!")

   