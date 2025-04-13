# Expense Tracker MVP

## Overview
The Expense Tracker is a web application designed to track expenses, categorize them, and visualize spending patterns. This Minimum Viable Product (MVP) allows users to add expenses, view a summary, and see visual insights through charts. It serves as a demonstration of basic expense tracking functionality.

### Features
- **Add Expenses**: Input expenses with date, amount, category, and description.
- **Expense List**: View all expenses in a table.
- **Summary**: See total expenses and average expense amount.
- **Visual Insights**:
  - Bar chart for expenses by category.
  - Line chart for running total over time.

## Technologies Used
- **Backend**: Python, Flask, Pandas
- **Frontend**: HTML, CSS (Bootstrap), JavaScript (Chart.js)
- **Data Storage**: CSV file (`data/expenses.csv`)

## Setup Instructions
1. **Prerequisites**:
   - Python 3.6+
   - Install dependencies:
     ```
     pip install flask pandas jinja2
     ```

2. **Clone the Repository** (if hosted on Git):
     ```
   git clone <repository-url>
   cd expense_tracker
     ```
3. **Run the Application**:
     ```
   python app.py
     ```
- The app will run at `http://127.0.0.1:5000/`.

4. **Directory Setup**:
- The app automatically creates a `data/` directory for `expenses.csv` if it doesn’t exist.

## Usage
1. **View Expenses**:
- Open `http://127.0.0.1:5000/` to see the expense list, summary, and charts.
2. **Add an Expense**:
- Click “Add Expense” in the navigation bar.
- Fill in the form (date, amount, category, description) and submit.
3. **Visualize Spending**:
- The “Expenses by Category” chart shows spending per category.
- The “Running Total Over Time” chart shows cumulative expenses over time.

## Known Issues
- Favicon 404 error: The app doesn’t include a favicon, causing a harmless 404 error in the console. Add a `favicon.ico` to `static/` if desired.
- Large numbers in charts may require scrolling due to fixed chart height.

## Contributing
This is a demonstration MVP. Contributions are welcome! Please fork the repository, make changes, and submit a pull request. Focus areas:
- Bug fixes
- UI/UX improvements

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.