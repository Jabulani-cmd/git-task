# List of items sold in the café
menu = ["coffee", "tea", "sandwich", "cake"]

# Dictionary containing the stock value for each item
stock = {
    "coffee": 100,  # 100 units of coffee in stock
    "tea": 150,     # 150 units of tea in stock
    "sandwich": 50, # 50 units of sandwiches in stock
    "cake": 30      # 30 units of cake in stock
}

# Dictionary containing the price for each item
price = {
    "coffee": 2.50,  # Price of one coffee
    "tea": 2.00,     # Price of one tea
    "sandwich": 5.00, # Price of one sandwich
    "cake": 3.50      # Price of one cake
}

# Initialize a variable to store the total stock worth
total_stock = 0

# Loop through the menu to calculate the total worth of the stock
for item in menu:
    # Calculate the value of the current item's stock
    item_value = stock[item] * price[item]
    
    # Add the item's value to the total stock worth
    total_stock += item_value

# Print the total worth of the stock
print(f"The total worth of the stock in the café is: R{total_stock:.2f}")