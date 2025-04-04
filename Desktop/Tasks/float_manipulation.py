# Import the statistics module
import statistics

# Initialize an empty list to store the floats
numbers = []

# Ask the user to input 10 floats
for i in range(10):
    while True:
        try:
            # Prompt the user for input and convert it to a float
            num = float(input(f"Enter float {i + 1}: "))
            numbers.append(num)
            break
        except ValueError:
            print("Invalid input. Please enter a valid float.")

# Calculate the total of all numbers
total = sum(numbers)
print(f"Total of all numbers: {total}")

# Find the index of the maximum number
max_index = numbers.index(max(numbers))
print(f"Index of the maximum number: {max_index}")

# Find the index of the minimum number
min_index = numbers.index(min(numbers))
print(f"Index of the minimum number: {min_index}")

# Calculate the average (mean) and round it to two decimal places
average = round(statistics.mean(numbers), 2)
print(f"Average of the numbers: {average}")

# Find the median number
median = statistics.median(numbers)
print(f"Median of the numbers: {median}")