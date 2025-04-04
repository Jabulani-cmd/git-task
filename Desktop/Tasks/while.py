# while.py

# Initialize variables
total = 0
count = 0

# Continuously ask the user to enter a number
while True:
    # Prompt the user for input
    user_input = input("Enter a number (or -1 to stop): ")

    # Check if the input is "-1" to stop the loop
    if user_input == "-1":
        break

    # Convert the input to a number
    try:
        number = float(user_input)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

    # Check if the number is 0 (invalid input)
    if number == 0:
        print("0 is not a valid input. Please enter another number.")
        continue

    # Add the valid number to the total and increment the count
    total += number
    count += 1

# Calculate the average (if at least one valid number was entered)
if count > 0:
    average = total / count
    print(f"The average of the valid numbers entered is: {average:.2f}")
else:
    print("No valid numbers were entered.")
    