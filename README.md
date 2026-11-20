💰 Expense Tracker

📌 About the Project

Expense Tracker is a console-based Python application designed to manage personal expenses. The application allows users to add, view, update, delete, and search expenses, calculate total spending, manage expense categories, and export expense records to a CSV file.

The project was developed using Python and demonstrates the use of modular programming, functions, file handling, JSON data storage, exception handling, and input validation.

✨ Features

Add Expense – Add a new expense with a title, amount, category, and date.

Show All Expenses – Display all saved expenses.

Edit Expense – Update the title, amount, or category of an existing expense.

Delete Expense – Remove an expense by its ID.

Search Expenses – Find a specific expense using its ID.

Total Expenses – Calculate the total amount of all expenses.

Show Categories – Display available expense categories.

Export to CSV – Export expense records to a CSV file.

📂 Project Structure

ExpenseTracker/
│
├── main.py
├── expenses.py
├── reports.py
├── storage.py
├── validation.py
├── exceptions.py
│
└── data/
    ├── expenses.json
    └── expenses.csv

File Description

File

Description

main.py

Main application file. Displays the menu and manages user interaction.

expenses.py

Contains expense management functions such as adding, updating, searching, retrieving, and deleting expenses.

reports.py

Contains reporting functions, including total expense calculation and CSV export.

storage.py

Handles reading and writing expense data using JSON.

validation.py

Validates expense titles, amounts, and categories.

exceptions.py

Contains custom error-handling functions.

data/expenses.json

Stores expense records in JSON format.

data/expenses.csv

Stores exported expense records in CSV format.

🛠️ Technologies Used

Python

JSON

CSV

UUID

DateTime

File Handling

Exception Handling

Modular Programming

📋 Expense Data Structure

Each expense is stored as a dictionary containing the following information:

{
    "id": "a1b2c3d4",
    "title": "Book",
    "amount": 25.0,
    "category": "Education",
    "date": "2026-11-20"
}

Data Fields

ID – Unique identifier assigned to each expense.

Title – Name or description of the expense.

Amount – Expense amount.

Category – Expense category.

Date – Date when the expense was recorded.

Expense IDs are generated using the uuid module to identify individual records.

🏷️ Expense Categories

The application includes the following predefined categories:

Food

Shopping

Education

Health

Entertainment

Other

Users can select a category when adding or updating an expense.

▶️ How to Run the Project

1. Clone the repository

git clone https://github.com/your-username/ExpenseTracker.git

2. Navigate to the project directory

cd ExpenseTracker

3. Run the application

python main.py

🖥️ Application Menu

========================================
          EXPENSE TRACKER
========================================

1. Add Expense
2. Show All Expenses
3. Edit Expense
4. Delete Expense
5. Search Expenses
6. Show Total Expenses
7. Show Categories
8. Export to CSV

0. Exit

========================================

Users interact with the application through a simple command-line menu.

🔒 Data Validation

The application validates user inputs before saving expense records.

Validation includes:

Expense title cannot be empty.

Amount must be numeric.

Amount must be greater than zero.

Category must belong to the predefined category list.

Invalid inputs are handled using exceptions to prevent incorrect data from being saved.

💾 Data Storage

Expense records are stored in a JSON file.

JSON provides a simple and readable format for storing structured data. The application loads existing expenses from the file and saves changes whenever an expense is added, updated, or deleted.

This allows expense records to remain available after the application is closed and restarted.

📊 CSV Export

The application supports exporting expense records to CSV format.

CSV files can be opened using spreadsheet applications such as Microsoft Excel, making it easier to review, organize, and analyze expense data.

🎯 Project Objectives

The main objectives of this project are:

Practice Python programming.

Apply modular programming principles.

Work with functions and data structures.

Implement CRUD operations.

Understand JSON and CSV file handling.

Practice input validation.

Use exception handling.

Organize a Python project into multiple modules.

Develop a practical application using real-world logic.

👩‍💻 Developer

Developed as a Python programming practice project to improve programming skills and apply fundamental concepts in a practical application.

📌 Future Improvements

Possible future improvements include:

Monthly expense reports.

Expense filtering by date.

Expense filtering by category.

Graphical user interface (GUI).

Budget management.

Income tracking.

More advanced statistics and charts.