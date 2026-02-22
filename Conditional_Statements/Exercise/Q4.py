a = int(input("Enter 1st number:"))
b = int(input("Enter 2nd number:"))
c = int(input("Enter 3rd number:"))

if (a > b and a > c):
    print("Greatest is 1st number:",a)
elif(b > a and b > c):
    print("Greatest is 2nd number:",b)
else:
    print("Greatest is 3rd number:",c)