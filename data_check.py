import sqlite3

db_name = "expense_tracker.db"

def check_data_in_tables(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    for month in range(1, 13):
        table_name = f"expenses_{month:02d}"
        cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
        count = cursor.fetchone()[0]
        print(f"Table {table_name} has {count} records.")

    conn.close()

check_data_in_tables(db_name)
