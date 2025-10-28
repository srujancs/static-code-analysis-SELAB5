"""Inventory Management System - Static Analysis Lab"""

import json
from datetime import datetime

# Global variable
stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """Add an item to the stock with specified quantity."""
    if logs is None:
        logs = []

    if not isinstance(item, str) or not isinstance(qty, int):
        print("Invalid input types for item or quantity.")
        return

    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(item, qty):
    """Remove a given quantity of an item from stock."""
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        print(f"Item '{item}' not found in inventory.")
    except TypeError:
        print("Quantity must be a number.")


def get_qty(item):
    """Return the quantity of a given item."""
    return stock_data.get(item, 0)


def load_data(file_path="inventory.json"):
    """Load stock data from a JSON file and return it."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print("File not found. Starting with empty stock.")
        return {}
    except json.JSONDecodeError:
        print("Invalid JSON format. Starting fresh.")
        return {}


def save_data(file_path="inventory.json"):
    """Save stock data to a JSON file."""
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(stock_data, file, indent=4)
    except IOError as err:
        print(f"Error saving data: {err}")


def print_data():
    """Print all items in stock."""
    print("Items Report:")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")


def check_low_items(threshold=5):
    """Return a list of low stock items."""
    return [item for item, qty in stock_data.items() if qty < threshold]


def main():
    """Main function to test inventory operations."""
    add_item("apple", 10)
    add_item("banana", 2)
    add_item("orange", 0)

    remove_item("apple", 3)
    remove_item("grapes", 1)

    print(f"Apple stock: {get_qty('apple')}")
    print(f"Low items: {check_low_items()}")

    save_data()
    load_data()
    print_data()


if __name__ == "__main__":
    main()
