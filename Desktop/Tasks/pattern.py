# pattern.py

# Number of rows for the top half of the arrow
rows = 5

# Top half of the arrow
for i in range(1, rows + 1):
    print("*" * i)

# Bottom half of the arrow
for i in range(rows - 1, 0, -1):
    print("*" * i)