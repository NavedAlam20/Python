year = int(input("Enter year: "))

if year % 400 == 0:
    print("Century Leap Year")
elif year % 100 == 0:
    print("Not a Leap Year")
elif year % 4 == 0:
    print("Regular Leap Year")
else:
    print("Not a Leap Year")