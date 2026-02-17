s1 = "apple"
s2 = "grape"

res = len(set(s1.lower()) & set(s2.lower()))
print(res) #3