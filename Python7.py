# OOP Inheritance Over Loading Overriding


class rectangle():
    def __init__(self,length,breadth) -> None:
        self.length=length
        self.breadth=breadth
    
    def getArea(self):
        print(self.length*self.breadth," is the area of rectangle")
    
    def print_message(self, message, language):
        print(f"Parent message in {language}: {message}")

class square(rectangle):
    def __init__(self,side,length,breadth) -> None:
        self.side=side
        super().__init__(length, breadth)
    
    def print_message(self, message):
        print(f"Child message: {message}")
    
    def print_message(self, message):
        args = [message]  # Explicitly declare and initialize args
        if len(args) == 1:  # Check for single argument
            print(f"Child message: {message}")
        else:  # Pass arguments to parent's method
            super().print_message(message, language)

    # def print_message(self, message, language):
    #     super().print_message(message,language)


child_object = square(2,5,7)

child_object.print_message("Hello from child")  # Calls the child class's version

#child_object.print_message("Hola from parent","Spanish")  # Calls the parent class's version explicitly

lst=list('12345678')
print(f"{lst}")

print(lst[::4]) # Meaning - print(lst[start:end:step])

print(lst[2:6:2])