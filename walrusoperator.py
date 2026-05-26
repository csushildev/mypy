# Without walrus operator
data = input("Enter a value (or 'quit' to exit): ")
while data != "quit":
    print(f"You entered: {data}")
    data = input("Enter a value (or 'quit' to exit): ")

# With walrus operator
while (data := input("Enter a value (or 'quit' to exit): ")) != "quit":
    print(f"You entered: {data}")


numbers = [1, 2, 3, 4, 5]

# Without walrus operator:  calculate x * 2 twice
results = [x * 2 for x in numbers if x * 2 > 5]

# With walrus operator: calculate x * 2 only once
results = [y for x in numbers if (y := x * 2) > 5]

# Without Walrus
with open("my_file.txt", "r") as f:
    line = f.readline()
    while line:
        print(line.strip())
        line = f.readline()

# With Walrus
with open("my_file.txt", "r") as f:
    while (line := f.readline()):
        print(line.strip())


        results = [y ]