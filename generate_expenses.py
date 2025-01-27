import random
from faker import Faker
import calendar
from datetime import datetime
from database_operations import create_database, store_expenses_in_db

fake = Faker()

def generate_expenses(month, year, num_entries=150):
    last_day = calendar.monthrange(year, month)[1]
    expenses = []

    for _ in range(num_entries):
        start_date = datetime(year, month, 1)
        end_date = datetime(year, month, last_day)

        # Generate a date within the selected month
        date = fake.date_between(start_date=start_date, end_date=end_date)

        amount = round(random.uniform(5, 500), 2)
        category = random.choice(["Bills", "Groceries", "Subscriptions", "Personal"])
        description = fake.sentence(nb_words=5)

        expenses.append((date, amount, category, description))

    print(f"Generated {num_entries} expenses for {year}-{month:02d}")  # Debugging
    return expenses


# Example usage: Generate expenses for January 2024
# print(generate_expenses(1, 2024, 150))  # Generates 150 entries for January 2024

# Store expenses in the database
# store_expenses_in_db(expenses, 1, 2024)  # Store expenses for January 2024
