# Ask the user to enter 3 different integers:
# Use the input() function to prompt the user to enter the first integer.
# Convert the input to an integer and save it in a variable (e.g., num1).
# Repeat the process for the second and third integers (num2 and num3).
# Perform calculations:
# Calculate the sum of all three numbers (num1 + num2 + num3).
# Calculate the first number minus the second number (num1 - num2).
# Calculate the third number multiplied by the first number (num3 * num1).
# Calculate the sum of all three numbers divided by the third number ((num1 + num2 + num3) / num3).
# Display the results of each calculation.

# Step 1: Ask the user to enter 3 different integers
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

# Step 2: Perform calculations
sum_all = num1 + num2 + num3
first_minus_second = num1 - num2
third_times_first = num3 * num1
sum_divided_by_third = sum_all / num3

# Step 3: Print out the results
print(f"The sum of all the numbers is: {sum_all}")
print(f"The first number minus the second number is: {first_minus_second}")
print(f"The third number multiplied by the first number is: {third_times_first}")
print(f"The sum of all three numbers divided by the third number is: {sum_divided_by_third}")