li = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
n = int(input("Enter number you want to find:"))
for i in li:
    # print(i)
    if (n == i):
        print("Found in the list")
        break
else:
    print("Not in List")