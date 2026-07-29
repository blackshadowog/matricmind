import os
import pandas as pd

# Current file: PROJECT-1/backend/database.py
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

# Project folder: PROJECT-1
PROJECT_DIR = os.path.dirname(CURRENT_DIR)

# Repository root: matricmind
ROOT_DIR = os.path.dirname(PROJECT_DIR)

# Database folder: matricmind/database
DATABASE_DIR = os.path.join(ROOT_DIR, "database")


def load_csv(filename):
    path = os.path.join(DATABASE_DIR, filename)

    if not os.path.exists(path):
        raise FileNotFoundError(f"CSV file not found: {path}")

    return pd.read_csv(path)


def load_all_tables():
    return {
        "customers": load_csv("metricmind_customers_table.csv"),
        "products": load_csv("metricmind_products_table.csv"),
        "orders": load_csv("metricmind_orders_table.csv"),
        "order_items": load_csv("metricmind_orderItems_table.csv"),
        "inventory": load_csv("metricmind_inventory_table.csv"),
        "expenses": load_csv("metricmind_expenses_table.csv"),
        "budgets": load_csv("metricmind_budgets_table.csv"),
        "returns": load_csv("metricmind_returns_table.csv"),
    }


if __name__ == "__main__":
    tables = load_all_tables()

    for name, df in tables.items():
        print(f"{name}: {df.shape}")