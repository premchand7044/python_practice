class StringReverser:
    def reverse_words(self, input_string):
        # Split the string into words
        words = input_string.split()

        # Reverse the order of words
        reversed_words = words[::-1]

        # Join the reversed words back into a string
        reversed_string = ' '.join(reversed_words)

        return reversed_string


# Example usage:
if __name__ == "__main__":
    reverser = StringReverser()

    try:
        input_str = input("Enter a string: ")
        reversed_result = reverser.reverse_words(input_str)
        print(f"Original string: {input_str}")
        print(f"Reversed string (word by word): {reversed_result}")
    except Exception as e:
        print(f"Error: {e}")
