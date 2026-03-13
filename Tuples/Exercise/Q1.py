a = [(1, 2), (), (3, 4), (), (5,)]
res = list(filter(None, a))
print(res) #[(1, 2), (3, 4), (5,)]