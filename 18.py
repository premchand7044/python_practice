class IntegerToRoman:
    def convert_to_roman(self, num):
        if not isinstance(num, int) or not 0 < num < 4000:
            raise ValueError("Input must be an integer between 1 and 3999")

        result = ""
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        numerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        for value, numeral in zip(values, numerals):
            while num >= value:
                result += numeral
                num -= value

        return result


# Example usage with user input:
if __name__ == "__main__":
    converter = IntegerToRoman()

    try:
        user_input = int(input("Enter an integer (1-3999): "))
        roman_numeral = converter.convert_to_roman(user_input)
        print(f"The Roman numeral representation of {user_input} is: {roman_numeral}")
    except ValueError as e:
        print(f"Error: {e}")
