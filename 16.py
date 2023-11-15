# copyfile.py

import os

# Prompt the user for the names of the files
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
input_file_name = os.path.join(desktop_path, input("Enter the name of the input text file: "))
output_file_name = os.path.join(desktop_path, input("Enter the name of the output text file: "))

try:
    # Open the input file for reading
    with open(input_file_name, 'r') as input_file:
        # Read the contents of the input file
        file_contents = input_file.read()

    # Open the output file for writing
    with open(output_file_name, 'w') as output_file:
        # Write the contents to the output file
        output_file.write(file_contents)

    print(f"Contents of '{input_file_name}' have been copied to '{output_file_name}' successfully.")
except FileNotFoundError:
    print(f"File '{input_file_name}' not found. Please make sure the input file exists.")
except Exception as e:
    print(f"An error occurred: {e}")
