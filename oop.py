class Employee:
    def __init__(self, name, salary, bond):
        self.name = name
        self.salary = salary
        self.bond = bond

    def display_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}, Bond: {self.bond}")

class Manager(Employee):
    def __init__(self, name, salary, bond, department):
        super().__init__(name, salary, bond)
        self.department = department

    def display_info(self):
        super().display_info()
        print(f"Department: {self.department}")

# Example usage
employee1 = Employee("Alice", 50000, "2 years")
manager1 = Manager("Bob", 80000, "3 years", "Sales")
employee1.display_info()
manager1.display_info()

#object introspection
print(dir(employee1))  # Output: <class '__main__.Employee'>
print(type(manager1))   # Output: <class '__main__.Manager'>
print(isinstance(employee1, Employee))  # Output: True
print(isinstance(manager1, Employee))   # Output: True
print(isinstance(manager1, Manager))    # Output: True