# Open and read the DOB.txt file
with open('DOB.txt', 'r') as file:
    lines = file.readlines()

# Initialize lists to store names and birthdates
names = []
birthdates = []

# Process each line in the file
for line in lines:
    # Split the line into parts
    parts = line.strip().split()
    
    # The name is the first two parts, and the birthdate is the remaining parts
    name = ' '.join(parts[:2])
    birthdate = ' '.join(parts[2:])
    
    # Append to the respective lists
    names.append(name)
    birthdates.append(birthdate)

# Print the names section
print("Name")
for name in names:
    print(name)

# Print the birthdates section
print("\nBirthdate")
for birthdate in birthdates:
    print(birthdate)