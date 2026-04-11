f = open("Demo.txt","w+")
print(f.read()) #This truncate a file and print Nothing
f.write("abc")#Added to empty file
f.close()