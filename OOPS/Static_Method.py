class Calc:
    @staticmethod
    def add(a, b): #@staticmethod makes add() independent of class objects.
        return a + b

res = Calc.add(2, 3) #Calc.add(2, 3) directly calls the method using the class name.
print(res) #5