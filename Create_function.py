'''
How to Create Function 
'''
#define function
def function():
    print("Have a nice day")
#call function
function()

print(20*"=","perimeter of square fuction")
#define dunction and create formula
def perimeter_square(a):
    p = a * 4
    print("perimeter of a square is :",p)
function() # call the function inside the other function
perimeter_square(2) # set input value 

print(20*"=","perimeter of rectangle fuction")
def perimeter_rectangle():
    l = 3
    w = 5
    p = 2*(l+w)
    print("if length is ",l,"and width is ",w)
    print("perimeter rectangle is :",p)
perimeter_rectangle()

print(20*"=","function argument")
#function using argument and keyword
def captain(name):#argument
    print("Captain of pirates:",name)
captain("luffy")#input of argument

def crew(name,ability): 
    print("One of crew :",name)
    print("Ability :", ability)
crew(name="zoro", ability="swords") #keywords()
crew(ability="cooking", name="sanji", ) #keywords()
crew("nami","navigator") #keywords()

#function using default
def emperor(name,power="dragon"): #set default
    print("one of emperor :",name)
    print("power :", power)
emperor("kaido")
emperor(name="big mom", power="soul")
#emperor(power="dragon") # will missing requirement positional "name".