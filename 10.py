# Input the number of rows for the pattern
num_rows = int(input("Enter the number of rows: "))

# Constructing a pattern of stars
for i in range(num_rows):
    for j in range(i + 1):
        print("*", end=" ")
    print()  # Move to the next line after each row
