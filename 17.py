# unique_words.py

def extract_unique_words(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            words = content.split()
            unique_words = set(words)
            return sorted(unique_words)
    except FileNotFoundError:
        print(f"File '{file_path}' not found. Please make sure the file exists.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Hardcoded file path for testing
file_path = r'C:\Users\master\Desktop\hi.txt'

# Extract and print unique words in alphabetical order
unique_words_list = extract_unique_words(file_path)
print("Unique words in alphabetical order:")
for word in unique_words_list:
    print(word)
