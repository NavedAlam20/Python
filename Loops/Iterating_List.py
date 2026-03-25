li = ["Welcome", "To","Python"]

for i in li:
    print(i) 
    #output
    '''
    Welcome
    To
    Python
    '''
#method 2 using range() method
for i in range(len(li)):
    print(li[i])
    #output
    '''
    Welcome
    To
    Python
    '''
#print in horizontal
for i in range(len(li)):
    print(li[i],end=" ") #Welcome TO Python