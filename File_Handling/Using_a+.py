f = open("Demo.txt","a+")
print(f.read())#Not truncate a file
f.write("ABC")#Append at the end
f.close()