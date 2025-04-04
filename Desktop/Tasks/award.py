# Step 1: Ask the user to input the times for each event
swimming_time = int(input("Enter the swimming time (in minutes): "))
cycling_time = int(input("Enter the cycling time (in minutes): "))
running_time = int(input("Enter the running time (in minutes): "))

# Step 2: Calculate the total time
total_time = swimming_time + cycling_time + running_time

# Step 3: Determine the award based on the total time
if total_time <= 100:
    award = "Provincial Colours"
elif 101 <= total_time <= 105:
    award = "Provincial Half Colours"
elif 106 <= total_time <= 110:
    award = "Provincial Scroll"
else:
    award = "No Award"

# Step 4: Output the total time and the award
print(f"\nTotal time to complete the triathlon: {total_time} minutes")
print(f"Award: {award}")