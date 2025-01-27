import sqlite3
import csv

def export_data_to_csv(db_name="expense_tracker.db", output_file="expenses_data.csv"):
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        with open(output_file, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(['id', 'date', 'amount', 'category', 'description'])

            for month in range(1, 13):  # From January to December
                table_name = f"expenses_{month:02d}"
                
                # Check if table exists before querying
                cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
                if cursor.fetchone() is None:
                    print(f"Skipping {table_name} as it doesn't exist.")
                    continue

                cursor.execute(f"SELECT * FROM {table_name};")
                rows = cursor.fetchall()

                for row in rows:
                    csv_writer.writerow(row)

        print(f"Data exported successfully to {output_file}")

    except sqlite3.Error as e:
        print(f"Error while exporting data: {e}")

    finally:
        conn.close()

# Example usage:
# export_data_to_csv()
