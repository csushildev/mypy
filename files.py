
file = open("my_file.txt","w")
file.write("Hello, World! \nThis is a test file.")
file.close()
file = open("my_file.txt","r")
content = file.read()
file.close()
print(content)


try:
    file = open("my_file.txt", "r")  # Open in read mode
    content = file.read()  # Read the entire file content
    print(content)
    file.close()  # Close the file
except FileNotFoundError:
    print("File not found.")


# Reading line by line
try:
    file = open("my_file.txt", "r")
    for line in file: # Efficient for large files
        print(line.strip()) # Remove newline characters
    file.close()
except FileNotFoundError:
    print("File not found.")


file = open("new_file.txt", "w")  # Open in write mode (creates or overwrites)
file.write("Hello, world!\n")  # Write some text
file.write("This is a new line.\n")
file.close()


file = open("my_file.txt", "a")  # Open in append mode
file.write("This is appended text.\n")
file.close()

try:
    with open("my_file.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found.")

with open("output.txt", "w") as file:
    file.write("Data written using 'with'.\n")