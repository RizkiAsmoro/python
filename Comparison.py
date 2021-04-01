'''
Simple comparison using input value and without if else condition
The data type must be set float because otherwise the input is of type data string
'''

val_a = float(input ('Insert Value a =')) 
val_b = float(input ('Insert Value b ='))

equalto = val_a == val_b
notequalto = val_a != val_b
more_than = val_a > val_b
less_than = val_a < val_b
lessthanequalto = val_a <= val_b 
morethanequalto = val_a >= val_b


print (val_a,'=',val_b,'=',equalto)
print (val_a,'!=',val_b,'=',notequalto)
print (val_a,'>',val_b,'=',more_than)
print (val_a,'<',val_b,'=',less_than)
print (val_a,'<=',val_b,'=',lessthanequalto)
print (val_a,'>=',val_b,'=',morethanequalto)

#compare 'is' and 'is not'
#is as object identity
#example x = 5, then x is object and 5 is literal
#hex is object storage in memory
#object must be compare with object
#if object compare with literal then will be SyntaxWarning
print ('=========Object indentity (is)')
x = 7
y = 9
identityis = x is y
print ('If value')
print ('value X =',x,'with id hex',hex(id(x)))
print ('value Y =',y,'with id hex',hex(id(y)))
print ('x is y =', identityis)

x = 7
y = 7
identityis = x is y
print ('If value')
print ('value X =',x,'with id hex',hex(id(x)))
print ('value Y =',y,'with id hex',hex(id(y)))
print ('x is y =', identityis)

print ('=========Object indentity (is not)')
x = 7
y = 9
identityis = x is not y
print ('If value')
print ('value X =',x,'with id hex',hex(id(x)))
print ('value Y =',y,'with id hex',hex(id(y)))
print ('x is not y =', identityis)

x = 7
y = 7
identityis = x is not y
print ('If value')
print ('value X =',x,'with id hex',hex(id(x)))
print ('value Y =',y,'with id hex',hex(id(y)))
print ('x is not y =', identityis)