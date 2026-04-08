# defining a function
def a(): 
  print("Python")
  
# assigning function to a variable
var=a

# calling the variable
var() #Python



#Function with Local and Global Variables
x = 123  # global variable

def display():
    x = 98  # local variable
    print(x)  
    print(globals()['x'])  # accesses global x

print(x) #123

a = display  # assign function to a variable
a()  # call function prints 98 and 123
a()  # call function prints 98 and 123