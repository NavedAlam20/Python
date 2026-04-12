try:
    file = open("Demo.txt", "r")
    Data = file.read()
    print(Data) #print the data in demo.txt file
finally:
    file.close()