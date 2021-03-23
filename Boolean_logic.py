'''
Operasi Boolean
NOT, OR, AND, XOR
Tabel kebenaran
'''
# Operation NOT
print ('======NOT=====')
a = True
b = not a
print ('Data A =', a)
print ('Data B =', b)

#Operation OR
print ('======OR=====')
a = True
b = True
c = a or b
print (a,'Or',b,'=',c)
a = True
b = False
c = a or b
print (a,'Or',b,'=',c)
a = False
b = True
c = a or b
print (a,'Or',b,'=',c)
a = False
b = False
c = a or b
print (a,'Or',b,'=',c)

#Operation OR
print ('======AND=====')
a = True
b = True
c = a and b
print (a,'And',b,'=',c)
a = True
b = False
c = a and b
print (a,'And',b,'=',c)
a = False
b = True
c = a and b
print (a,'And',b,'=',c)
a = False
b = False
c = a and b
print (a,'And',b,'=',c)

#Operation OR
print ('======XOR=====')
a = True
b = True
c = a ^ b
print (a,'XOR',b,'=',c)
a = True
b = False
c = a ^ b
print (a,'XOR',b,'=',c)
a = False
b = True
c = a ^ b
print (a,'XOR',b,'=',c)
a = False
b = False
c = a ^ b
print (a,'XOR',b,'=',c)


