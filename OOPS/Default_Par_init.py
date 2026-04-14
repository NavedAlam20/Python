class Dog:
    def __init__(self, name, breed="Mixed", age=1): #breed="Mixed" and age=1 are default values.
        self.name = name
        self.breed = breed
        self.age = age

d1 = Dog("Buddy")
d2 = Dog("Max", "Golden Retriever", 5) #the defaults are overwritten by the provided values.
print(d1.name, d1.breed, d1.age) #Buddy Mixed 1
print(d2.name, d2.breed, d2.age) #Max Golden Retriever 5