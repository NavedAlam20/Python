# Typecasting list into set
li = [1, 2, 3, 3, 4, 5, 5, 6, 2]
s = set(li)
print(s) #{1, 2, 3, 4, 5, 6}

# Typecasting string into set
s = "WelcomeToPython"
s = set(s)
print(s) #{'P', 'y', 'n', 'o', 'T', 'm', 'h', 'l', 'c', 'e', 't', 'W'}

# Typecasting dictionary into set
d = {1: "One", 2: "Two", 3: "Three"}
s = set(d)
print(s) #{1, 2, 3}