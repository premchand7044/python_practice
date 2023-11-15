class PowerCalculator:
    def power(self, x, n):
        # Check if n is a non-negative integer
        if not isinstance(n, int) or n < 0:
            raise ValueError("Exponent must be a non-negative integer")

        result = 1
        for _ in range(n):
            result *= x

        return result


# Example usage:
if __name__ == "__main__":
    calculator = PowerCalculator()

    try:
        base = float(input("Enter the base (x): "))
        exponent = int(input("Enter the exponent (n): "))
        result = calculator.power(base, exponent)
        print(f"{base} raised to the power of {exponent} is: {result}")
    except ValueError as e:
        print(f"Error: {e}")
