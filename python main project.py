import os
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate

# Database Initialization
def init_db():
    conn = sqlite3.connect("finance_tracker.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS transactions (
                        id INTEGER PRIMARY KEY,
                        date TEXT,
                        category TEXT,
                        amount REAL,
                        type TEXT
                    )''')
    conn.commit()
    conn.close()

# Add Transaction
def add_transaction(date, category, amount, trans_type):
    conn = sqlite3.connect("finance_tracker.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO transactions (date, category, amount, type) VALUES (?, ?, ?, ?)",
                   (date, category, amount, trans_type))
    conn.commit()
    conn.close()

# View Transactions
def view_transactions():
    conn = sqlite3.connect("finance_tracker.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM transactions")
    rows = cursor.fetchall()
    conn.close()
    print(tabulate(rows, headers=["ID", "Date", "Category", "Amount", "Type"], tablefmt="grid"))

# Generate Report
def generate_report():
    conn = sqlite3.connect("finance_tracker.db")
    df = pd.read_sql_query("SELECT * FROM transactions", conn)
    conn.close()

    if df.empty:
        print("No transactions to report.")
        return

    df['amount'] = df['amount'].astype(float)
    report = df.groupby(['type', 'category'])['amount'].sum().unstack(fill_value=0)
    print("\nFinancial Summary:\n")
    print(tabulate(report, headers="keys", tablefmt="grid"))

    # Plotting
    report.T.plot(kind='bar', stacked=True, figsize=(10, 6))
    plt.title('Financial Summary by Category')
    plt.ylabel('Amount')
    plt.xlabel('Category')
    plt.tight_layout()
    plt.show()

# Main Menu
def main():
    init_db()
    while True:
        print("\nPersonal Finance Tracker")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Generate Report")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category (e.g., Food, Rent, Entertainment): ")
            amount = float(input("Enter amount: "))
            trans_type = input("Enter type (Income/Expense): ").capitalize()
            add_transaction(date, category, amount, trans_type)
            print("Transaction added successfully.")

        elif choice == '2':
            view_transactions()

        elif choice == '3':
            generate_report()

        elif choice == '4':
            print("Exiting. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
