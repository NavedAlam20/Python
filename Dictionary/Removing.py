d = {1: 'Welcome', 2: 'To', 3: 'Python', 'age':22}

# Using del 
del d["age"]
print(d) #{1: 'Welcome', 2: 'To', 3: 'Python'}

# Using pop() 
val = d.pop(1)
print(val) #Welcome

# Using popitem()
key, val = d.popitem()
print(f"Key: {key}, Value: {val}") #Key: 3, Value: Python

# Using clear()
d.clear()
print(d) #{}