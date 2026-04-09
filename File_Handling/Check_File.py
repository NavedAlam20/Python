f = open("Demo.txt", "r")
print("Filename:", f.name)#Demo.txt
print("Mode:", f.mode)#r
print("Is Closed?", f.closed)#False

f.close()
print("Is Closed?", f.closed)#True