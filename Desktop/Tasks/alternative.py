# Function to alternate character case
def alternate_character_case(input_string):
    result = ""
    for i, char in enumerate(input_string):
        if i % 2 == 0:
            result += char.upper()  # Uppercase for even indices
        else:
            result += char.lower()  # Lowercase for odd indices
    return result

# Function to alternate word case
def alternate_word_case(input_string):
    words = input_string.split()  # Split the string into words
    for i in range(len(words)):
        if i % 2 == 0:
            words[i] = words[i].lower()  # Lowercase for even indices
        else:
            words[i] = words[i].upper()  # Uppercase for odd indices
    return " ".join(words)  # Join the words back into a single string

# Main program
if __name__ == "__main__":
    # Prompt the user to enter a string
    user_input = input("Enter a string: ")

    # Task 1: Alternate character case
    alternate_char_result = alternate_character_case(user_input)
    print("Alternate Character Case:", alternate_char_result)

    # Task 2: Alternate word case
    alternate_word_result = alternate_word_case(user_input)
    print("Alternate Word Case:", alternate_word_result)