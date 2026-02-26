a = []
#using append()
a.append(10)  
print("After append(10):", a)  
#using insert()
a.insert(0, 5)
print("After insert(0, 5):", a) 
#using extend()
a.extend([15, 20, 25])  
print("After extend([15, 20, 25]):", a) 
#clear() -> removes all items
a.clear()
print("After clear():", a)

"""output

After append(10): [10]
After insert(0, 5): [5, 10]
After extend([15, 20, 25]): [5, 10, 15, 20, 25]
After clear(): []"""