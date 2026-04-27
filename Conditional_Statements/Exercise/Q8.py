a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

D = b**2 - 4*a*c

if D > 0:
    print("Real and Distinct Roots")
elif D == 0:
    print("Real and Equal Roots")
else:
    print("Complex Roots")