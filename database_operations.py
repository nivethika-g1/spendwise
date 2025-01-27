import sqlite3
import calendar

def create_database(db_name="expense_tracker.db"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Create tables for each month from January to December
    for month in range(1, 13):
        table_name = f"expenses_{month:02d}"
        cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                amount REAL NOT NULL,
                category TEXT NOT NULL,
                description TEXT
            );
        """)
        print(f"✅ Table {table_name} checked/created.")  # Debugging

    conn.commit()
    conn.close()
    print("✅ Database and tables created successfully.")

# Run this function manually
create_database()

def store_expenses_in_db(expenses, month, db_name="expense_tracker.db"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    table_name = f"expenses_{month:02d}"

    for expense in expenses:
        cursor.execute(f"""
            INSERT INTO {table_name} (date, amount, category, description)
            VALUES (?, ?, ?, ?);
        """, (expense[0], expense[1], expense[2], expense[3]))

    conn.commit()
    conn.close()
    print(f"✅ Data inserted into {table_name} successfully.")

#store_expenses_in_db()

import sqlite3

def check_existing_tables(db_name="expense_tracker.db"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # List all tables in the database
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    conn.close()

    # Print the table names
    print("Existing tables in the database:", [table[0] for table in tables])

# Run this function manually
check_existing_tables()
