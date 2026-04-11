f = open("Demo.txt","r+")#Read + Write
f.write("abc")#Overwrite from start and not truncate the file
f.close()