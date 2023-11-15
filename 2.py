# Input two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Addition
addition_result = num1 + num2
print("Addition:", addition_result)

# Subtraction
subtraction_result = num1 - num2
print("Subtraction:", subtraction_result)

# Multiplication
multiplication_result = num1 * num2
print("Multiplication:", multiplication_result)

# Division
# Check if the denominator is not zero
if num2 != 0:
    division_result = num1 / num2
    print("Division:", division_result)
else:
    print("Division by zero is not allowed.")

# Floor Division
floor_division_result = num1 // num2
print("Floor Division:", floor_division_result)

# Modulus (Remainder)
# Check if the denominator is not zero
if num2 != 0:
    modulus_result = num1 % num2
    print("Modulus:", modulus_result)
else:
    print("Modulus by zero is not allowed.")

# Exponentiation
exponentiation_result = num1 ** num2
print("Exponentiation:", exponentiation_result)
