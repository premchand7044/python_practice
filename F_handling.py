# Creating and writing to a file
new_content = "Hello, this is some content for the file."
with open('sample.txt', 'w') as file:
    file.write(new_content)

# Reading from a file
file = open('sample.txt', 'r')  # 'r' stands for read mode
content = file.read()
print(content)
file.close()