#using for loop
n = int(input("Enter a number for table:"))
for i in range(1,11):
    print(f'{n} * {i} = {n*i}')
    
#using while loop
n = int(input("Enter a number for table:"))
i = 0
while (i<=10):
    print(f'{n} * {i} = {n*i}')
    i += 1