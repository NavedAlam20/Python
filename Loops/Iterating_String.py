s = "abc"

for i in s:
    print(i) 
    #output
    '''
    a
    b
    c
    '''
#method 2 using range() method
for i in range(len(s)):
    print(s[i])
    #output
    '''
    a
    b
    c
    '''
#print in horizontal
for i in range(len(s)):
    print(s[i],end=" ") #a b c