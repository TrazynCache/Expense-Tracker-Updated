import pandas as pd

#Reads expenses from CSV file. Return empty if non-existent.
def read_expenses(file_path):
    try:
        df = pd.read_csv(file_path, parse_dates=['date'])
        return df
    except (FileNotFoundError, pd.errors.EmptyDataError):
        df = pd.DataFrame(columns=['date', 'amount', 'category', 'description'])
        df['date'] = pd.to_datetime(df['date'], errors='coerce') # Ensure datetime type.
        return df

#Appends new expense to CSV file.
def write_expense(file_path, expense):
    df = read_expenses(file_path) 
    new_row = pd.DataFrame([expense])
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv(file_path, index=False)