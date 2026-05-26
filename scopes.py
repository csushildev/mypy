 
def modify_global():
    global x
    x = 5  # Modifies the global x
 
modify_global()
x = 10  # Global variable

print(x)  # Output: 5