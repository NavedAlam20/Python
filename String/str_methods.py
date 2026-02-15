s = "Hello"
print(len(s)) # 5

a = "Hello World"
print(a.upper()) # HELLO WORLD
print(a.lower()) # hello world

b = "   Hlo   "
print(b.strip())  # Hlo without space 

c = "Python is fun"
print(c.replace("fun", "awesome")) # Python is awesome

str = "I am a coder"

print(str.endswith("er")) # return True if string ends with substr
print(str.capitalize()) # capatalizes 1st character
print(str.find ("a")) # return 1st index of 1st occurrence
print(str.count("am")) # count the occurence of substring