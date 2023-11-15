# Function to check if a triangle is a right triangle
def is_right_triangle(side1, side2, side3):
    # Sort the sides in ascending order
    sides = [side1, side2, side3]
    sides.sort()

    # Check the Pythagorean theorem
    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        return True
    else:
        return False

# Input the lengths of the three sides
side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

# Check if it's a right triangle
if is_right_triangle(side1, side2, side3):
    print("It's a right triangle!")
else:
    print("It's not a right triangle.")
