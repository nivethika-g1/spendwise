import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns

# Connect to the database
db_path = "expense_tracker.db"  # Adjust path if needed
conn = sqlite3.connect(db_path)

# Load the data
@st.cache  # Caching data to improve performance
def load_data():
    months = [f"expenses_{str(i).zfill(2)}" for i in range(1, 13)]
    df_list = []

    for month in months:
        query = f"SELECT * FROM {month}"
        temp_df = pd.read_sql(query, conn)
        temp_df["month"] = month
        df_list.append(temp_df)

    df = pd.concat(df_list, ignore_index=True)
    df["date"] = pd.to_datetime(df["date"])
    return df

df = load_data()

# Display Data
st.title("Expense Tracker")
st.write("This is an expense tracker app that shows insights into spending patterns.")
st.dataframe(df.head())  # Show the first few rows of the data

# Summary Statistics Section
st.header("Summary Statistics")
st.write(df.describe())

# Monthly Spending Section
st.header("Total Monthly Spending")
monthly_spending = df.groupby("month")["amount"].sum()
st.bar_chart(monthly_spending)

# Spending Breakdown by Category Section
st.header("Spending Breakdown by Category")
category_spending = df.groupby("category")["amount"].sum().sort_values(ascending=False)
st.write(category_spending)

# Visualize Spending Breakdown by Category
st.subheader("Category Spending Pie Chart")
fig, ax = plt.subplots(figsize=(8, 8))
category_spending.plot(kind="pie", autopct="%1.1f%%", cmap="coolwarm", ax=ax)
st.pyplot(fig)

# Top Spending Days
st.header("Top Spending Days")
highest_spend_days = df.groupby("date")["amount"].sum().sort_values(ascending=False)
st.write(highest_spend_days.head(10))

# Close database connection
conn.close()
