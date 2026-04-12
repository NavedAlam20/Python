with open("Practice.txt","r") as f:#open in read mode
    data = f.read() #read the data and store in data var

new_data = data.replace("Java", "Python")#replace the Java with Python using replace() and store in new data
print(new_data)

with open("Practice.txt","w") as f:#open in write mode to overwrite
    f.write(new_data)#overwrite replace data using new data var
