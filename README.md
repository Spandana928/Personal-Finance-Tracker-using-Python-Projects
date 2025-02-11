Personal Finance Tracker

Overview

The Personal Finance Tracker is a simple command-line application that helps users manage their finances efficiently. It allows users to record transactions, view a summary of their income and expenses, and generate financial reports with graphical insights.

Features

Add Transactions: Record income or expenses with date, category, and amount.

View Transactions: Display all recorded transactions in a tabular format.

Generate Reports: Summarize financial data by category and type (income/expense).

Graphical Insights: Visual representation of financial data using bar charts.

Technologies Used

Python (Core language)

SQLite3 (Database for storing transactions)

Pandas (Data manipulation and analysis)

Matplotlib (Graphical visualization)

Tabulate (Formatted table display in the console)

Installation

Clone the repository:

git clone https://github.com/yourusername/finance-tracker.git
cd finance-tracker

Install required dependencies:

pip install pandas matplotlib tabulate

Run the application:

python finance_tracker.py

Usage

Add a Transaction:

Enter date, category, amount, and type (Income/Expense).

View Transactions:

Displays all recorded transactions in a tabular format.

Generate Report:

Provides a summary of income and expenses, along with a graphical representation.

Exit:

Stops the application.

Example Output

+----+------------+-------------+--------+---------+
| ID | Date       | Category    | Amount | Type    |
+----+------------+-------------+--------+---------+
|  1 | 2025-02-10 | Food        |  20.5  | Expense |
|  2 | 2025-02-11 | Salary      | 5000.0 | Income  |
+----+------------+-------------+--------+---------+

Contribution

Feel free to contribute by submitting issues or pull requests.

License

This project is licensed under the MIT License.

Author
Spandana L
