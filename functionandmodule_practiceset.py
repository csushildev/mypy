'''Write a function greet() that prints "Hello, Python Learner!" when
called.
Write a function square(num) that returns the square of a given number. Test
it with different numbers.
'''

def greet():
    print("Hello, Python Learner!")

def square(num):
    return num ** 2

# Test the functions
greet()
print(square(5))
print(square(10))

#firstname = input("Enter your first name: ")
#lastname = input("Enter your last name: ")

#lambda_fullname = lambda fname, lname: f"{fname} {lname}"
#print(lambda_fullname(firstname, lastname))

##
def calculate_area(length, width=10):
    return length * width

print("area of rectangle :"+str(calculate_area(5)))  # Uses default width

## 

square = lambda x: x * x
list1 = [1, 2, 3, 4, 5]
print(list(map(square,list1)))


## factorial using recursion
def factorial(n):
    if n ==0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

def sum_of_digits(n):
    if n == 0:
        return 0
    return n%10 + sum_of_digits(n // 10)

print(sum_of_digits(1234))

import requests

a = requests.get("https://api.github.com")
print(a.json())

numberset = (list(range(1, 25)));
evenlist = list(filter(lambda x: x % 2 == 0,numberset))
print(evenlist)




def lambdasqrt(x):
    if x % 2==0:
        return True
    else:
        return False

listeven=list(filter(lambdasqrt,numberset))
print(listeven)