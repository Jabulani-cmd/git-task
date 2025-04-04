#1. Save the sentence "The!quick!brown!fox!jumps!over!the!lazy!dog." as a string.

#2. Use the replace() function to replace all ! with a space.

#3. Print the modified sentence: "The quick brown fox jumps over the lazy dog."

#4. Use the upper() function to convert the sentence to uppercase.

#5. Print the uppercase sentence: "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG."

#6. Use slicing ([::-1]) to reverse the sentence.

#7. Print the reversed sentence.

# Step 1: Save the original sentence
original_sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog."

# Step 2: Replace "!" with a space
modified_sentence = original_sentence.replace("!", " ")

# Step 3: Print the modified sentence
print(modified_sentence)  # Output: "The quick brown fox jumps over the lazy dog."

# Step 4: Convert the sentence to uppercase
uppercase_sentence = modified_sentence.upper()

# Step 5: Print the uppercase sentence
print(uppercase_sentence)  # Output: "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG."

# Step 6: Reverse the sentence using slicing
reversed_sentence = uppercase_sentence[::-1]

# Step 7: Print the reversed sentence
print(reversed_sentence)  # Output: ".GOD YZAL EHT REVO SPMUJ XOF NWORB KCIUQ EHT"