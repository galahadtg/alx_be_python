# pattern_drawing.py

# Prompt the user for input
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Outer loop (while loop for rows)
while row < size:
    # Inner loop (for loop for columns)
    for col in range(size):
        print("*", end="")  # print * without newline
    print()  # move to next row
    row += 1
