# Create a list
my_list = [1, 2, 3, 4, 5]
print("Initial List:", my_list)

# Append elements to the list
my_list.append(6)
my_list.append(7)
print("List after appending elements:", my_list)

# Remove elements from the list
# Remove element by value
my_list.remove(3)
print("List after removing element 3:", my_list)

# Remove element by index
removed_element = my_list.pop(1)
print("List after removing element at index 1:", my_list)
print("Removed element:", removed_element)

# Clear the entire list
my_list.clear()
print("List after clearing all elements:", my_list)
