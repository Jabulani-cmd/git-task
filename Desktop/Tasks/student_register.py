# Ask the user how many students are registering
num_students = int(input("How many students are registering? "))

# Open the reg_form.txt file in write mode
with open('reg_form.txt', 'w') as file:
    # Loop for the number of students
    for i in range(num_students):
        # Ask the user to enter the student ID
        student_id = input(f"Enter student ID for student {i + 1}: ")
        
        # Write the student ID to the file
        file.write(f"Student ID: {student_id}\n")
        
        # Add a dotted line for the student to sign
        file.write("................................\n")

print("Registration complete. Check reg_form.txt for the attendance register.")