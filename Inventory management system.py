import csv

# File to store inventory data
INVENTORY_FILE = "inventory.csv"

# Initialize the inventory file if it doesn't exist
def initialize_file():
    try:
        with open(INVENTORY_FILE, mode="x", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Item Name", "Quantity", "Price"])
    except FileExistsError:
        pass

# Function to display the inventory
def display_inventory():
    print("\n--- Inventory ---")
    try:
        with open(INVENTORY_FILE, mode="r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header
            items = list(reader)

            if items:
                print(f"{'Item Name':<20}{'Quantity':<10}{'Price':<10}")
                print("-" * 40)
                for row in items:
                    print(f"{row[0]:<20}{row[1]:<10}{row[2]:<10}")
            else:
                print("Inventory is empty.")
    except FileNotFoundError:
        print("Inventory file not found. Initializing a new inventory file.")
        initialize_file()

# Function to add a new item to the inventory
def add_item():
    item_name = input("Enter item name: ").strip()
    quantity = input("Enter quantity: ").strip()
    price = input("Enter price: ").strip()

    try:
        with open(INVENTORY_FILE, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([item_name, quantity, price])
        print(f"Item '{item_name}' added successfully!")
    except Exception as e:
        print(f"Error adding item: {e}")

# Function to update an existing item's quantity
def update_item():
    item_name = input("Enter the item name to update: ").strip()
    try:
        with open(INVENTORY_FILE, mode="r") as file:
            reader = csv.reader(file)
            items = list(reader)

        for i, row in enumerate(items):
            if i == 0:  # Skip header
                continue
            if row[0].lower() == item_name.lower():
                new_quantity = input(f"Enter new quantity for '{item_name}': ").strip()
                row[1] = new_quantity
                with open(INVENTORY_FILE, mode="w", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerows(items)
                print(f"Quantity for '{item_name}' updated successfully!")
                return

        print(f"Item '{item_name}' not found in inventory.")
    except FileNotFoundError:
        print("Inventory file not found. Initializing a new inventory file.")
        initialize_file()
    except Exception as e:
        print(f"Error updating item: {e}")

# Function to delete an item from the inventory
def delete_item():
    item_name = input("Enter the item name to delete: ").strip()
    try:
        with open(INVENTORY_FILE, mode="r") as file:
            reader = csv.reader(file)
            items = list(reader)

        for i, row in enumerate(items):
            if i == 0:  # Skip header
                continue
            if row[0].lower() == item_name.lower():
                items.pop(i)
                with open(INVENTORY_FILE, mode="w", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerows(items)
                print(f"Item '{item_name}' deleted successfully!")
                return

        print(f"Item '{item_name}' not found in inventory.")
    except FileNotFoundError:
        print("Inventory file not found. Initializing a new inventory file.")
        initialize_file()
    except Exception as e:
        print(f"Error deleting item: {e}")

# Main menu for the inventory system
def main_menu():
    while True:
        print("\n--- Inventory Management System ---")
        print("1. Display Inventory")
        print("2. Add Item")
        print("3. Update Item Quantity")
        print("4. Delete Item")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            display_inventory()
        elif choice == "2":
            add_item()
        elif choice == "3":
            update_item()
        elif choice == "4":
            delete_item()
        elif choice == "5":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    initialize_file()
    main_menu()
python