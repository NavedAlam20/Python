class Person:
    def __init__(self, name, age): #name and age: parameters passed when creating the object.
        self.name = name #object attributes that store these values.
        self.age = age

p1 = Person("Naved", 21)
p2 = Person("Faizan", 22)

print(p1.name, p1.age)  # Naved 21
print(p2.name, p2.age)  # Faizan 22