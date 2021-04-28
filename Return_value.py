'''
Function Return Value
so that the function can be used again
'''
def multiplication(value1, value2):
    total = value1 * value2
    print("a.",value1, "x", value2, "=",total)
    return total
def sum(value1, value2):
    total = value1 + value2
    print("b.",value1, "+", value2, "=",total)
    return total

a = multiplication(2, 5)
b = sum(3, 4)
c = a - b
d = multiplication(a, b)
e = sum(a, multiplication(a, b))
print("a =",a) 
print("b =",b) 
print("a - b =",c) #the function can be used again and print
print("a x b =",d)
print("sum value of a and result multiplication between a and b =",e)
