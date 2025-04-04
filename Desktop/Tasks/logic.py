# Program to calculate the average of two numbers
def calculate_average(num1, num2):
    # Fixed Logical Error: Correct formula for calculating the average
    average = (num1 + num2) / 2  # Parentheses ensure the sum is calculated before division
    return average

# Input two numbers
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

# Calculate the average
result = calculate_average(number1, number2)

# Display the result
print(f"The average of {number1} and {number2} is: {result}")