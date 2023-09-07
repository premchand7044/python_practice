# Creating an empty stack using a list
stack = []

# Adding elements to the stack
stack.append(5)
stack.append(10)
stack.append(15)

print(stack)  # Output: [5, 10, 15]

# Removing and printing elements from the stack
top_item = stack.pop()  # Removing and getting the top item (15)
print(top_item)  # Output: 15

print(stack)  # Output: [5, 10]
