dic = [
    {"name": "Harry", "age": 20},
    {"name": "Robin", "age": 20},
    {"name": "Kevin", "age": 19}
]

print("Sorted by age:")
print(sorted(dic, key=lambda x: x['age']))

#output

''' Sorted by age:
[{'name': 'Kevin', 'age': 19}, {'name': 'Harry', 'age': 20}, {'name': 'Robin', 'age': 20}]'''
