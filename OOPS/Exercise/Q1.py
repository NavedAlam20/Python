class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        n = len(self.marks)
        sum = 0
        for i in range(n):
            sum += self.marks[i]
        avg = sum/n
        return avg


s1 = Student("Naved",[77, 88, 91])
print(s1.average())