from functools import wraps
# Sample Set
fruits = {"apple", "banana", "orange"}
# Sets are unordered collections of unique elements.
# They are useful for removing duplicates and performing set operations like union, intersection, and difference.

# Sample List
numbers = [1, 2, 3, 4, 5]
# Lists are ordered collections that can contain duplicate elements.
# They are versatile and commonly used for storing and manipulating data.

# Sample Dictionary
student = {"name": "John", "age": 20, "grade": "A"}
# Dictionaries are key-value pairs where each key is unique.
# They are useful for storing and retrieving data based on a specific key, like a real-life dictionary.

# Sample Tuple
coordinates = (10, 20)
# Tuples are ordered collections that can contain any type of data.
# They are immutable, meaning their values cannot be changed once defined.
# Tuples are useful for representing fixed collections of related values.


def logger_decorator(func):
    """
    Decorator function that adds logging functionality to the decorated function.
    It prints the name of the function being called before and after executing it.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} execution completed")
       # print (result)
        return result
    return wrapper


@logger_decorator
def square_numbers(numbers):
    """
    Function that squares each number in the given list and returns a list of squared numbers.
    """
    print("Squaring numbers...")
    squares = []
    for num in numbers:
        squares.append(num ** 2)
       # print(squares)
    return squares


numbers = [1, 2, 3, 4, 5]
result = square_numbers(numbers)
print(result)

#
# now what is the *args (list of non-keyword arguments) and **kwargs (dictionary of keyword arguments) in python
# 

def print_inf(*args) -> None:
    for num in args:
        print(f"{num}")

print_inf(1,2,3)

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="John", age=25, city="New York")
