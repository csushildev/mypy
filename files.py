
file = open("my_file.txt","w")
file.write("Hello, World! \nThis is a test file.")
file.close()
file = open("my_file.txt","r")
content = file.read()
file.close()
print(content)