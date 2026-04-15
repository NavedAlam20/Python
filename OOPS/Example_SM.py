class Check:
    @staticmethod
    def is_even(n): #is_even() works independently and does not access any class data.
        return n % 2 == 0

print(Check.is_even(10)) #True