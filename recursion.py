#fibonacci series

a=0
b=1



def fib(n):
    if n==1 or n==0:
        return n
    else:
        return fib(n-1) + fib(n-2)

print(fib(10))
