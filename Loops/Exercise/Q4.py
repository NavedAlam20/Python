#using for loop without indexing traverse
li = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for i in li:
    print(i, end=" ")

#using while loop with index traversing
li = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
i = 0
n = len(li)
while (i < n):
    print(li[i],end=" ")
    i += 1