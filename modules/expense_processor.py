# Calculate the total sum of all values in the 'amount' column of the DataFrame.
def calculate_total(df):
    return df['amount'].sum()

# Compute the average expense amount by dividing the total sum of the 'amount' column by the number of expenses in the DataFrame.
def calculate_average(df):
    return df['amount'].mean()

# Sort the DataFrame by date and calculate the cumulative sum of the 'amount' column to show the running total of expenses over time, returning an empty DataFrame if the input is empty.
def calculate_running_total(df):
    df = df.sort_values(by='date')
    df['running_total'] = df['amount'].cumsum()
    return df