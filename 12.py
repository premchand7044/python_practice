# Function to calculate factorial using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Input the number
num = int(input("Enter a number to calculate its factorial: "))

# Check for non-negative input
if num < 0:
    print("Factorial is undefined for negative numbers.")
else:
    # Calculate and print the factorial
    result = factorial(num)
    print(f"The factorial of {num} is: {result}")
