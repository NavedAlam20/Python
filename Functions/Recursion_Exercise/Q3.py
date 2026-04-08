def print_list(list, index = 0):
    if(index == len(list)):
        return
    print(list[index], end = " ")#print items of a list in a one line
    print_list(list, index+1)

fruits = ["Mango", "Banana", "Kiwi", "Avacado"]
print_list(fruits)