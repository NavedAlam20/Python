#Dictionary keys() Method
d = {'Name': 'Naved', 'Age': '21', 'Country': 'India'}
print(list(d.keys())) #['Name', 'Age', 'Country']

#Dictionary values() Method
print(list(d.values())) #['Naved', '21', 'India']

#Dictionary get() Method
print(d.get('Name')) #Naved
print(d.get('Gender')) #None

#Dictionary items() Method
print(list(d.items())[1][0]) #Age
print(list(d.items())[1][1]) #21

#Dictionary pop() Method
d.pop('Age')
print(d) #{'Name': 'Naved', 'Country': 'India'}

#Dictionary popitem() Method
val = d.popitem()
print(val) #('Country', 'India')

#Dictionary update() Method
d1 = {'Name': 'Naved', 'Age': '21', 'Country': 'India'}
d2 = {'Name': 'Faizan', 'Age': '22'}

d1.update(d2)
print(d1) #{'Name': 'Faizan', 'Age': '22', 'Country': 'India'}

#Dictionary clear() Method
d1.clear()
print(d1) #{}
 