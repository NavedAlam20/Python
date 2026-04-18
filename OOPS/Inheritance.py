class Animal: #Defines the parent class.
    def __init__(self, name):
        self.name = name

    def info(self): #Prints the name of the animal.
        print("Animal name:", self.name)

class Dog(Animal): #Defines Dog as a child of Animal class.
    def sound(self):
        print(self.name, "barks")

d = Dog("Buddy")
d.info() #Calls parent method info()      Inherited method
d.sound() #Calls child method.