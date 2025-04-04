"""
Nike Warehouse Management System

This program helps manage shoe inventory with various operations
including viewing, adding, searching, and analyzing stock data.
"""


class Shoe:
    """Class to represent each shoe product in inventory."""

    def __init__(self, country, code, product, cost, quantity):
        """
        Initialize shoe attributes.

        Args:
            country (str): Origin country of shoe
            code (str): Unique product code
            product (str): Name of shoe product
            cost (float): Unit cost of shoe
            quantity (int): Current stock quantity
        """
        self.country = country
        self.code = code
        self.product = product
        self.cost = float(cost)
        self.quantity = int(quantity)

    def get_cost(self):
        """Return the cost of the shoe."""
        return self.cost

    def get_quantity(self):
        """Return the current quantity in stock."""
        return self.quantity

    def __str__(self):
        """Return string representation of shoe for file storage."""
        return f"{self.country},{self.code},{self.product},{self.cost},{self.quantity}"


# Global list to store all shoe objects
shoe_list = []


def read_shoes_data():
    """Read shoe data from inventory.txt and create Shoe objects."""
    try:
        with open('inventory.txt', 'r', encoding='utf-8') as file:
            next(file)  # Skip header row
            for line in file:
                data = line.strip().split(',')
                if len(data) == 5:  # Verify correct number of fields
                    shoe_list.append(Shoe(*data))
    except FileNotFoundError:
        print("\nError: inventory.txt not found. Please ensure the file exists.")
    except Exception as e:
        print(f"\nError reading file: {e}")


def capture_shoes():
    """Allow user to input new shoe data and add to inventory."""
    print("\n╔════════════════════════════╗")
    print("║    ADD NEW SHOE PRODUCT    ║")
    print("╚════════════════════════════╝")
    try:
        country = input("Country: ")
        code = input("Product Code: ")
        product = input("Product Name: ")
        cost = float(input("Cost: "))
        quantity = int(input("Quantity: "))

        shoe_list.append(Shoe(country, code, product, cost, quantity))
        print(f"\nSuccessfully added {product} to inventory!")
    except ValueError:
        print("\nInvalid input. Please enter numbers for cost and quantity.")


def view_all():
    """Display all shoes in inventory in formatted table."""
    if not shoe_list:
        print("\nNo shoes in inventory. Please load data first.")
        return

    # Header with f-strings
    header = f"\n{'Country':<15} {'Code':<10} {'Product':<20} {'Cost':<10} {'Quantity':<10}"
    separator = "-" * 65
    print(f"{header}\n{separator}")

    for shoe in shoe_list:
        print(f"{shoe.country:<15} {shoe.code:<10} {shoe.product:<20} "
              f"${shoe.cost:<9.2f} {shoe.quantity:<10}")


def re_stock():
    """Find lowest quantity item and allow restocking."""
    if not shoe_list:
        print("\nNo shoes in inventory. Please load data first.")
        return

    lowest = min(shoe_list, key=lambda x: x.quantity)
    print(f"\nLowest stock item: {lowest.product} (Only {lowest.quantity} remaining)")

    while True:
        choice = input("Would you like to restock this item? (y/n): ").lower()
        if choice == 'y':
            try:
                add = int(input(f"Enter quantity to add to {lowest.product}: "))
                if add > 0:
                    lowest.quantity += add
                    update_file()
                    print(f"\nSuccessfully added {add} units. New quantity: {lowest.quantity}")
                    break
                print("\nQuantity must be positive.")
            except ValueError:
                print("\nPlease enter a valid number.")
        elif choice == 'n':
            print("\nRestock cancelled.")
            break
        else:
            print("\nPlease enter 'y' or 'n'.")


def search_shoe():
    """Search for shoe by product code and display details."""
    if not shoe_list:
        print("\nNo shoes in inventory. Please load data first.")
        return

    code = input("\nEnter product code to search: ").strip().upper()
    found = [shoe for shoe in shoe_list if shoe.code.upper() == code]

    if found:
        shoe = found[0]
        print(f"""
Product Found:
Product: {shoe.product}
Country: {shoe.country}
Code: {shoe.code}
Cost: ${shoe.cost:.2f}
Quantity: {shoe.quantity}""")
    else:
        print("\nNo product found with that code.")


def value_per_item():
    """Calculate and display total value for each product."""
    if not shoe_list:
        print("\nNo shoes in inventory. Please load data first.")
        return

    print(f"\n{'Product':<20} {'Total Value':<15}")
    print("-" * 35)

    for shoe in shoe_list:
        value = shoe.cost * shoe.quantity
        print(f"{shoe.product:<20} ${value:<15.2f}")


def highest_qty():
    """Identify and recommend product with highest quantity for sale."""
    if not shoe_list:
        print("\nNo shoes in inventory. Please load data first.")
        return

    highest = max(shoe_list, key=lambda x: x.quantity)
    print(f"""
SALE RECOMMENDATION:
Product: {highest.product}
Current Stock: {highest.quantity} units
Consider putting this item on sale!""")


def update_file():
    """Save current inventory data back to file."""
    try:
        with open('inventory.txt', 'w', encoding='utf-8') as file:
            file.write("Country,Code,Product,Cost,Quantity\n")
            for shoe in shoe_list:
                file.write(f"{shoe}\n")
    except Exception as e:
        print(f"\nError saving file: {e}")


def main_menu():
    """Main program loop with menu interface."""
    read_shoes_data()

    while True:
        menu = """
╔════════════════════════════╗
║  NIKE WAREHOUSE MANAGER    ║
╠════════════════════════════╣
║ 1. View All Products       ║
║ 2. Add New Product         ║
║ 3. Restock Low Inventory   ║
║ 4. Search Product          ║
║ 5. Assess Inventory Value  ║
║ 6. Check Overstocked Items ║
║ 7. Exit                    ║
╚════════════════════════════╝"""
        print(menu)

        try:
            choice = int(input("\nEnter your choice (1-7): "))

            if choice == 1:
                view_all()
            elif choice == 2:
                capture_shoes()
            elif choice == 3:
                re_stock()
            elif choice == 4:
                search_shoe()
            elif choice == 5:
                value_per_item()
            elif choice == 6:
                highest_qty()
            elif choice == 7:
                update_file()
                print("\nThank you for using Nike Warehouse Manager!")
                print("Goodbye!")
                break
            else:
                print("\nInvalid choice. Please enter a number between 1-7.")
        except ValueError:
            print("\nPlease enter a valid number.")


if __name__ == "__main__":
    print("\nWelcome to Nike Warehouse Management System!")
    main_menu()