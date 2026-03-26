capitals = {
    "India" : "New Delhi",
    "USA" : "Washington D.C",
    "Russia" : "Moscow",
    "China" : "Beijing",
    "Japan" : "Tokyo"
}

for key in capitals.keys():
    print(key) #Prints all keys
    
for value in capitals.values():
    print(value) #Prints all values
    
for key, value in capitals.items():
    print(key, "->", value) #Prints all key and corresponding values