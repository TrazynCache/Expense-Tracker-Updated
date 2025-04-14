import pandas as pd
import os

# Reads expenses from CSV file. Return empty if non-existent.
def read_expenses(file_path):
    try:
        df = pd.read_csv(file_path)
        df['date'] = pd.to_datetime(df['date'], errors='coerce')
        return df
    except (FileNotFoundError, pd.errors.EmptyDataError):
        df = pd.DataFrame(columns=['date', 'amount', 'category', 'description'])
        df['date'] = pd.to_datetime(df['date'], errors='coerce')
        return df

# Appends new expense to CSV file.
def write_expense(file_path, expense):
    df = read_expenses(file_path)
    new_row = pd.DataFrame([expense])
    df = pd.concat([df, new_row], ignore_index=True)
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    df.to_csv(file_path, index=False)

# Helper function to format and add a new expense
def add_expense(amount, date, category, description):
    expense = {
        'date': pd.to_datetime(date),  # Ensure date is datetime
        'amount': float(amount),
        'category': category,
        'description': description
    }
    write_expense('data/expenses.csv', expense)