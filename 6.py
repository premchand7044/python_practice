# Creating a tuple
my_tuple = (1, 2, 3, 'a', 'b', 'c')
print("Original Tuple:", my_tuple)

# Accessing elements in a tuple
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

# Slicing a tuple
sliced_tuple = my_tuple[2:5]
print("Sliced Tuple:", sliced_tuple)

# Concatenating tuples
tuple1 = (10, 20, 30)
tuple2 = ('x', 'y', 'z')
concatenated_tuple = tuple1 + tuple2
print("Concatenated Tuple:", concatenated_tuple)

# Tuple unpacking
x, y, z = tuple1
print("Unpacked values:", x, y, z)

# Finding the length of a tuple
tuple_length = len(my_tuple)
print("Length of the Tuple:", tuple_length)

# Checking if an element exists in a tuple
element_to_check = 'a'
if element_to_check in my_tuple:
    print(f"'{element_to_check}' exists in the tuple.")
else:
    print(f"'{element_to_check}' does not exist in the tuple.")
