# String Data Type

s = 'Welcome to the Python World'
print(s)

# check data type 
print(type(s))

# access string with index
print(s[1])# e
print(s[2])# l
print(s[-1])# d

# List Data Type

# Empty list
a = []

# list with int values
a = [1, 2, 3]
print(a) # [1,2,3]

# list with mixed values int and String
b = ["Welcome", "To", "Python", 4, 5]
print(b) # ['Welcome', 'To', 'Python', 4, 5]

# Access List Items

a = ["Welcome", "To", "Python"]
print("Accessing element from the list")
print(a[0]) # Welcome
print(a[2]) # Python

print("Accessing element using negative indexing")
print(a[-1]) # Python
print(a[-3]) # Welcome

# Tuple Data Type

# initiate empty tuple
tup1 = ()

tup2 = ('Welcome', 'Python')
print("\nTuple with the use of String: ", tup2) # Tuple with the use of String:  ('Welcome', 'Python')

tup3 = (1, 2, 3, 4, 5)

# access tuple items
print(tup3[0]) # 1
print(tup3[-1]) # 5
print(tup3[-3]) # 3