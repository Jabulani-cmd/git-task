def largest_number(numbers):
    # Base case: If the list has only one element, return it
    if len(numbers) == 1:
        return numbers[0]
    
# Recursive case: Compare the first element with the largest in the rest of the list
    first = numbers[0]
    largest_in_rest = largest_number(numbers[1:])
    return first if first > largest_in_rest else largest_in_rest

# Test cases
print(largest_number([1, 4, 5, 3]))          # Output: 5
print(largest_number([3, 1, 6, 8, 2, 4, 5]))  # Output: 8