# Initialize an empty list to store incorrect names
incorrect_names = []

# Loop until the user enters "John"
while True:
    # Ask the user to enter their name
    name = input("Enter your name: ").strip()  # Remove extra spaces
    
    # Check if the name is "John" (case-insensitive)
    if name.lower() == "john":
        break  # Exit the loop if "John" is entered
    
    # Add the incorrect name to the list
    incorrect_names.append(name)

# Print the list of incorrect names
print("Incorrect names:", incorrect_names)