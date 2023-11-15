# Creating a dictionary
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
print("Original Dictionary:", my_dict)

# Accessing values in a dictionary
print("Name:", my_dict['name'])
print("Age:", my_dict['age'])
print("City:", my_dict['city'])

# Modifying values in a dictionary
my_dict['age'] = 26
print("Updated Age:", my_dict['age'])

# Adding a new key-value pair
my_dict['gender'] = 'Male'
print("Updated Dictionary:", my_dict)

# Removing a key-value pair
removed_value = my_dict.pop('city')
print("Dictionary after removing 'city':", my_dict)
print("Removed value:", removed_value)

# Checking if a key exists in a dictionary
key_to_check = 'name'
if key_to_check in my_dict:
    print(f"'{key_to_check}' exists in the dictionary.")
else:
    print(f"'{key_to_check}' does not exist in the dictionary.")

# Iterating through key-value pairs in a dictionary
print("Iterating through the dictionary:")
for key, value in my_dict.items():
    print(f"{key}: {value}")
