# pattern_drawing.py

# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize a counter for the while loop
row = 0

# Use a while loop to iterate through each row
while row < size:
    # Use a for loop to print asterisks in each row
    for _ in range(size):
        print("*", end="")
    # Move to the next line after printing each row
    print()
    row += 1
