from abc import ABC, abstractmethod

# Abstract class
class Animal(ABC): #blueprint (cannot be instantiated directly)

    @abstractmethod
    def sound(self):
        pass

# Child class
class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

# Usage
d = Dog()
print(d.sound())   # Output: Bark