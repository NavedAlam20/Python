a = [10, 20, 30, 40, 50]
#remove()
a.remove(30)  
print("After remove(30):", a)
#pop()
popped_val = a.pop(1)  
print("Popped element:", popped_val)
print("After pop(1):", a) 
#del statement
del a[0]  
print("After del a[0]:", a)

#output

"""After remove(30): [10, 20, 40, 50]
Popped element: 20
After pop(1): [10, 40, 50]
After del a[0]: [40, 50]"""
