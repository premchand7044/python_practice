from collections import deque

# Creating an empty queue using a deque
queue = deque()

# Adding elements to the queue
queue.append(5)
queue.append(10)
queue.append(15)

print(queue)  # Output: deque([5, 10, 15])

# Removing and printing elements from the queue
front_item = queue.popleft()  # Removing and getting the front item (5)
print(front_item)  # Output: 5

print(queue)  # Output: deque([10, 15])
