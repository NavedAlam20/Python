class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def Hello(self):
        print("Hello", self.name, "Welcome to python")
    
    def get_marks(self):
        return self.marks

s1 = Student("Naved", 75)
s1.Hello()
print("Marks is :",s1.get_marks())