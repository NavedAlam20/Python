# Arithmetic Operators
a = 15
b = 4

# Addition
print("Addition:", a + b) # 19

# Subtraction
print("Subtraction:", a - b) # 11

# Multiplication
print("Multiplication:", a * b) # 60

# Division
print("Division:", a / b) # 3.75

# Floor Division
print("Floor Division:", a // b) # 3

# Modulus
print("Modulus:", a % b) # 3

# Exponentiation
print("Exponentiation:", a ** b) # 50625

# Comparison Operators
x = 13
y = 33

print(x > y) # False
print(x < y) # True
print(x == y) # False
print(x != y) # True
print(x >= y) # False
print(x <= y) # True

# Logical Operators
m = True
n = False
print(m and n) # False
print(m or n) # True
print(not m) # False

# Bitwise Operators
o = 10
p = 4

print(o & p) # 0
print(o | p) # 14
print(~o) # -11
print(o ^ p) # 14
print(o >> 2) # 2
print(o << 2) # 40

# Assignment Operators
r = 10
t = r
print(t) # 10
t += r
print(t) # 20
t -= r
print(t) # 10
t *= r
print(t) # 100
t <<= r
print(t) # 102400

# Identity Operators
j = 10
k = 20
l = j

print(j is not k) # True
print(j is l) # True