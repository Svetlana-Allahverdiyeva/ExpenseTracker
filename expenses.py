import uuid
from datetime import date
from storage import *
from validation import *
from exceptions import expensesNotFound

# CRUD operations

def addExpense(title, amount, category):
    expenses = loadExpenses()

    expense = {
        "id": str(uuid.uuid4())[:8],
        "title": validateTitle(title),
        "amount": validateAmount(amount),
        "category": validateCategory(category),
        "date": date.today().isoformat()
        
    }

    expenses.append(expense)
    saveExpenses(expenses)
    return expense

def getAllExpenses():
    return loadExpenses()

def searchExpense(expenseID):
    expenses = loadExpenses()
    for expense in expenses:
        if expense["id"] == expenseID:
            return expense
    expensesNotFound()

def updateExpense(expenseID, title, amount, category):
        expenses = loadExpenses()

        for expense in expenses:
            if expense["id"] == expenseID:
                expense["title"] = validateTitle(title)
                expense["amount"] = validateAmount(amount)
                expense["category"] = validateCategory(category)
                
                saveExpenses(expenses)
                return expense
        expensesNotFound()

def deleteExpense(expenseID):
    expenses = loadExpenses()
    for expense in expenses:
        if expense["id"] == expenseID:
            expenses.remove(expense)
            saveExpenses(expenses)
            return expense

    expensesNotFound()