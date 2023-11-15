# main_program.py
from my_module import greet

# Input the name
name = input("Enter your name: ")

# Use the imported function
greeting_message = greet(name)

# Print the greeting
print(greeting_message)
