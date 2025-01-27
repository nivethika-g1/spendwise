import streamlit as st
import sqlite3
import calendar

def query_expenses(month, db_name="expense_tracker.db"):
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        table_name = f"expenses_{month:02d}"

        # Debugging
        print(f"Querying data from {table_name}")

        cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
        if cursor.fetchone() is None:
            st.error(f"Table {table_name} does not exist.")
            conn.close()
            return []

        cursor.execute(f"SELECT category, SUM(amount) FROM {table_name} GROUP BY category;")
        results = cursor.fetchall()
        conn.close()

        return results
    except sqlite3.Error as e:
        st.error(f"Error querying the database: {e}")
        return []

# Streamlit interface
st.title("Expense Tracker")

# Dropdown to select month
month = st.selectbox("Select Month", list(range(1, 13)), format_func=lambda x: calendar.month_name[x])

# Get the expenses for the selected month
expenses = query_expenses(month)

# Display the results
if expenses:
    st.write(f"Total Expenses for {calendar.month_name[month]}:")
    expense_data = [{"Category": category, "Total": f"${total:.2f}"} for category, total in expenses]
    st.table(expense_data)
else:
    st.write("No data available for the selected month.")
