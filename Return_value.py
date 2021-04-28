'''
Function Return Value
so that the function can be used again
'''
def SquarePerimeter(argument):
    total = argument * 4
    print("-a box with each side of",argument,"cm then the perimeter is", total)
    return total
a = SquarePerimeter(2)
print("-Value",a) #the function can be used again and print

print(30*"=")

def multiplication(value1,value2):
    total : value1 * value2
    print(value1,"x",value2,"=",total)
    return total 
x = multiplication(4,3)
print(x)