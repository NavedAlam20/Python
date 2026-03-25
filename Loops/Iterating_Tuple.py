tup = ("Welcome", "To","Python")

for i in tup:
    print(i) 
    #output
    '''
    Welcome
    To
    Python
    '''
#method 2 using range() method
for i in range(len(tup)):
    print(tup[i])
    #output
    '''
    Welcome
    To
    Python
    '''
#print in horizontal
for i in range(len(tup)):
    print(tup[i],end=" ") #Welcome TO Python