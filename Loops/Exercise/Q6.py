#using while loop
n = int(input("Enter number:"))
sum = 0
i = 0
while (i<=n):
    sum += i
    i += 1
    
print("Total Sum:",sum) #take input 7 gives output 28 0+1+2+3+4+5+6+7 = 28

#using for loop
x = int(input("Enter number:"))
sum1 = 0
for i in range(0,n+1):
    sum1 += i
print("Total Sum:",sum1) #take input 5 gives output 15 0+1+2+3+4+5 = 15