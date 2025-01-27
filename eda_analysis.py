import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Connect to the database
db_path = "expense_tracker.db"  # Adjust path if needed
conn = sqlite3.connect(db_path)

# Load all 12 tables into a single DataFrame
months = [f"expenses_{str(i).zfill(2)}" for i in range(1, 13)]  # expenses_01 to expenses_12
df_list = []

for month in months:
    query = f"SELECT * FROM {month}"
    temp_df = pd.read_sql(query, conn)
    temp_df["month"] = month  # Add month column for tracking
    df_list.append(temp_df)

# Combine all months into one DataFrame
df = pd.concat(df_list, ignore_index=True)

# Convert 'date' column to datetime
df["date"] = pd.to_datetime(df["date"])

# Display first few rows
print("Sample Data:")
print(df.head())

# Summary Statistics
print("\n--- Summary Statistics ---")
print(df.describe())

# Total Monthly Spending
monthly_spending = df.groupby("month")["amount"].sum()
print("\nTotal Spending Per Month:")
print(monthly_spending)

# Visualize Monthly Spending Trend
plt.figure(figsize=(10, 5))
sns.barplot(x=monthly_spending.index, y=monthly_spending.values, palette="autumn")
plt.xticks(rotation=45)
plt.xlabel("Month")
plt.ylabel("Total Spend")
plt.title("Total Monthly Spending")
plt.show()

# Top Spending Categories
category_spending = df.groupby("category")["amount"].sum().sort_values(ascending=False)
print("\nTop Spending Categories:")
print(category_spending.head(10))

# Pie Chart of Spending by Category
plt.figure(figsize=(8, 8))
category_spending.plot(kind="pie", autopct="%1.1f%%", cmap="coolwarm")
plt.title("Spending Breakdown by Category")
plt.ylabel("")
plt.show()

# Spending per Category Over Time
category_trends = df.groupby(["month", "category"])["amount"].sum().unstack()

plt.figure(figsize=(12, 6))
category_trends.plot(kind="bar", stacked=True, colormap="coolwarm", figsize=(12, 6))
plt.xlabel("Month")
plt.ylabel("Total Spending")
plt.title("Category-Wise Monthly Spending")
plt.xticks(rotation=45)
plt.legend(title="Category", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.show()

# Highest Spending Days
highest_spend_days = df.groupby("date")["amount"].sum().sort_values(ascending=False)
print("\nTop Spending Days:")
print(highest_spend_days.head(10))

# Spending Trend Over Time
plt.figure(figsize=(12, 6))
df.groupby("date")["amount"].sum().plot(kind="line", marker="o", color="purple")
plt.xlabel("Date")
plt.ylabel("Total Spending")
plt.title("Daily Spending Trend")
plt.grid(True)
plt.show()

# Top 10 Highest Transactions
top_transactions = df.nlargest(10, "amount")
print("\nTop 10 Biggest Transactions:")
print(top_transactions)

# Average Daily and Monthly Spending
avg_daily_spending = df.groupby("date")["amount"].sum().mean()
avg_monthly_spending = df.groupby("month")["amount"].sum().mean()

print(f"\nAverage Daily Spending: ₹{avg_daily_spending:.2f}")
print(f"Average Monthly Spending: ₹{avg_monthly_spending:.2f}")

# Close database connection
conn.close()
