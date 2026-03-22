# Creating a frozenset from a list
fs = frozenset([1, 2, 3, 4, 5])
print(fs) #frozenset({1, 2, 3, 4, 5})

# Creating a frozenset from a set
s = {3, 1, 4, 1, 5}
fs = frozenset(s)
print(fs) #frozenset({1, 3, 4, 5})