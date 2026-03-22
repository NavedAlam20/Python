# Using Remove Method
s = {1, 2, 3, 4, 5}
s.remove(3)
print(s) #{1, 2, 4, 5}

# Using discard() Method
s.discard(4)
print(s) #{1, 2, 5}

# Attempting to discard an element that does not exist
s.discard(10)  # No error raised
print(s) #{1, 2, 5}

# Using pop() Method

a = {1, 2, 3, 4, 5}
val = a.pop()
print(val) #1
print(a) #{2, 3, 4, 5}