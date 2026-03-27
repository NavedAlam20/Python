i = 0
while (i <= 5):
    if(i == 3):
        i += 1
        continue
    print(i) #prints 0 to 5 except 3
    i += 1

#using for loop
s = "welcometopython"
for i in s:
    if (i == "e" or i == "o"):
        continue
    print(i) #prints all character except e and o