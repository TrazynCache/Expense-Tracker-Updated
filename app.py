from re import S
from flask import Flask, render_template, request, redirect, url_for
from modules.data_handler import read_expenses, add_expense as add_expense_data
from modules.expense_processor import calculate_total, calculate_average, calculate_running_total
import pandas as pd
import os

app = Flask(__name__)
CSV_FILE = 'data/expenses.csv'

@app.route('/')
def index():
    df = read_expenses(CSV_FILE)
    total = calculate_total(df)
    average = calculate_average(df) if not df.empty else 0
    category_totals = df.groupby('category')['amount'].sum()
    categories = category_totals.index.tolist()
    amounts = category_totals.values.tolist()
    if not df.empty:
        df_running = calculate_running_total(df)
        dates = df_running['date'].dt.strftime('%Y-%m-%d').tolist()
        running_totals = df_running['running_total'].tolist()
        # Format dates for display without time
        df['date_display'] = df['date'].dt.strftime('%Y-%m-%d')
    else:
        dates = []
        running_totals = []
        df['date_display'] = pd.Series(dtype='str')
    expenses = df.to_dict(orient='records')
    return render_template('index.html',
                          expenses=expenses,
                          total=total,
                          average=average,
                          categories=categories,
                          amounts=amounts,
                          dates=dates,
                          running_totals=running_totals)

@app.route('/add', methods=['GET', 'POST'])
def add_expense():
    if request.method == 'POST':
        amount = request.form['amount']
        date = request.form['date']
        category = request.form['category']
        description = request.form['description']
        add_expense_data(amount, date, category, description)
        return redirect(url_for('index'))
    df = read_expenses('data/expenses.csv')
    categories = sorted(df['category'].dropna().unique().tolist())
    return render_template('add_expense.html', categories=categories)

@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit_expense(index):    
    df = read_expenses(CSV_FILE)
    if index < 0 or index >= len(df):
        return redirect(url_for('index'))
    if request.method == 'POST':
        df.iloc[index] = {
            'date': pd.to_datetime(request.form['date']),
            'amount': float(request.form['amount']),
            'category': request.form['category'],
            'description': request.form['description']
        }
        os.makedirs(os.path.dirname(CSV_FILE), exist_ok=True)
        df.to_csv(CSV_FILE, index=False)
        return redirect(url_for('index'))
    expense = df.iloc[index].to_dict()
    expense['date_display'] = pd.to_datetime(expense['date']).strftime('%Y-%m-%d')
    categories = sorted(df['category'].dropna().unique().tolist())
    return render_template('edit_expense.html', expense=expense, index=index, categories=categories)

@app.route('/delete/<int:index>', methods=['POST'])
def delete_expense(index):
    df = read_expenses(CSV_FILE)
    if 0 <= index < len(df):
        df = df.drop(index).reset_index(drop=True)
        os.makedirs(os.path.dirname(CSV_FILE), exist_ok=True)
        df.to_csv(CSV_FILE, index=False)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)