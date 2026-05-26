'''
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
'''

def repeat(n):
    def decorator(func):
        def wrapper(a):
            for i in range(n):
                func(a)
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet("world")



def uppercase(func):
    def wrapper():
        return func().upper()
    return wrapper

def exclaim(func):
    def wrapper():
        return func() + "!!!"
    return wrapper

@uppercase
@exclaim
def greet():
    return "hello"

print(greet())