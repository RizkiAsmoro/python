'''
How to Create Function 
'''
#define function
def function():
    print("Have a nice day")
#call function
function()

print(20*"=","perimeter square fuction")
#define dunction and create formula
def perimeter_square(a):
    p = a * 4
    print("perimeter of a square is :",p)
function() # call the function inside the other function
perimeter_square(2) # set input value 

print(20*"=","perimeter rectangle fuction")
def perimeter_rectangle():
    l = 3
    w = 5
    p = 2*(l+w)
    print("if length is ",l,"and width is ",w)
    print("perimeter rectangle is :",p)
perimeter_rectangle()