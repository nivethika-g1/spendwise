
from generate_expenses import generate_expenses
from database_operations import create_database, store_expenses_in_db

# Step 1: Create the database and tables
create_database()

# Step 2: Generate expenses and store them for ALL 12 months
for month in range(1, 13):
    expenses = generate_expenses(month, 2024, 150)
    store_expenses_in_db(expenses, month)  # Ensure all months are stored
    print(f"✅ Stored {len(expenses)} expenses for {month:02d}/2024")
