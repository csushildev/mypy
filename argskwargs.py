def my_function(*args):
    print(type(args))  # <class 'tuple'>
    for arg in args:
        print(arg)

my_function(1, 2, 3, "hello")  # Output: 1 2 3 hello
my_function()  # No output (empty tuple)
my_function("a", "b")  # Output: a b

def my_function(**kwargs):
    print(kwargs)  # <class 'dict'>
    for key, value in kwargs.items():
        print(f"{key}: {value}")

my_function(name="Alice", age=30, city="New York")
# Output:
# name: Alice
# age: 30
# city: New York

my_function()  # No output (empty dictionary)
my_function(a=1, b=2)
# Output:
# a: 1
# b: 2