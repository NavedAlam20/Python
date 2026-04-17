class Employee:
    def __init__(self, name, salary):
        self.name = name          # Public attribute, can be accessed directly.
        self.__salary = salary    # Private attribute, cannot be accessed directly.

emp = Employee("Faizan", 50000)
print(emp.name)     #  Faizan 
print(emp.__salary)  #ERROR! Raises an error because __salary is private and hidden.