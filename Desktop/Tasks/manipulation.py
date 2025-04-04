#1. Ask the user to enter a sentence:
#2. Calculate and display the length of str_manip:
#3. Find the last letter in str_manip:
#4. Replace every occurrence of the last letter with 'Q':
#5. Print the last 3 characters in str_manip backwards:
#6. Create a five-letter word using the first 3 and last 2 characters:

# Step 1: Ask the user to enter a sentence
str_manip = input("Please enter a sentence: ")

# Step 2: Calculate and display the length of str_manip
length = len(str_manip)
print(f"The length of the sentence is: {length}")

# Step 3: Find the last letter in str_manip
last_letter = str_manip[-1]
print(f"The last letter in the sentence is: '{last_letter}'")

# Step 4: Replace every occurrence of the last letter with 'Q'
modified_str = str_manip.replace(last_letter, 'Q')
print(f"The modified sentence is: {modified_str}")

# Step 5: Print the last 3 characters in str_manip backwards
last_three_backwards = str_manip[-1:-4:-1]
print(f"The last 3 characters in reverse are: {last_three_backwards}")

# Step 6: Create a five-letter word using the first 3 and last 2 characters
five_letter_word = str_manip[:3] + str_manip[-2:]
print(f"The five-letter word is: {five_letter_word}")