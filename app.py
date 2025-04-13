from flask import Flask, render_template, request, redirect, url_for
from modules.data_handler import read_expenses, write_expense
from modules.expense_processor import calculate_total, calculate_average, calculate_running_total
import pandas as pd

app = Flask(__name__)
CSV_FILE = 'data/expenses.csv'

@app.route('/')
def index():
    #Display the main page with expenses, summaries, and charts.
    df = read_expenses(CSV_FILE)
    total = calculate_total(df)
    average = calculate_average(df) if not df.empty else 0
    category_totals = df.groupby('category')['amount'].sum()
    categories = category_totals.index.tolist()  # Category names
    amounts = category_totals.values.tolist()    # Category totals
    if not df.empty:
        df_running = calculate_running_total(df)
        dates = df_running['date'].dt.strftime('%Y-%m-%d').tolist()
        running_totals = df_running['running_total'].tolist()
    else:
        dates = []
        running_totals = []
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
    #Handle adding a new expense via a form.
    if request.method == 'POST':
        date = request.form['date']
        amount = request.form['amount']
        category = request.form['category']
        description = request.form['description']
        try:
            date = pd.to_datetime(date)
            amount = float(amount)
            if amount < 0:
                raise ValueError("Amount cannot be negative")
        except ValueError as e:
            return f"Invalid input: {e}", 400
        expense = {'date': date, 'amount': amount, 'category': category, 'description': description}
        write_expense(CSV_FILE, expense)
        return redirect(url_for('index'))
    return render_template('add_expense.html')

if __name__ == '__main__':
    app.run(debug=True)