#Type 1 - Default argumnet
def fun(x, y=20):
    print("X:",x)
    print("Y:",y)

fun(10)#X:10 , Y:20

# Type 2 - Keyword Arguments
def student(fname, lname):
    print(fname, lname)

student(fname = "Naved", lname = "Alam")#Naved Alam
student(lname = "Alam", fname = "Naved")#Naved Alam 

# Type 3 - Positional Arguments
def nameAge(name, age):
    print("Hi, I am", name)
    print("My age is ", age)

nameAge("Naved", 21)#Hi, I am Naved : My age is  21
nameAge(21, "Naved")#Hi, I am 21 : My age is  Naved