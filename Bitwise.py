'''
Bitwise Operation
Operation each bit
example : int 1 = 00000001
          int 2 = 00000010
          int 9 = 00001001
'''
a = 8
b = 5
c = a | b
# Bitwise OR (|)
print ('=============OR============')
print ('    int:',a,',binary:',format(a,'08b'))  
print ('    int:',b,',binary:',format(b,'08b'))
print ('-----------------------------(|)') # operation OR
print ('bitwise:',c,',binary:',format(c,'08b'))

# Bitwise AND (&)
c = a & b
print ('=============AND============')
print ('    int:',a,',binary:',format(a,'08b'))  
print ('    int:',b,',binary:',format(b,'08b'))
print ('-----------------------------(&)') # operation AND
print ('bitwise:',c,',binary:',format(c,'08b'))

# Bitwise XOR
c = a ^ b
print ('=============XOR============')
print ('    int:',a,',binary:',format(a,'08b'))  
print ('    int:',b,',binary:',format(b,'08b'))
print ('-----------------------------(^)') # operation XOR
print ('bitwise:',c,',binary:',format(c,'08b'))

# Bitwise NOT (~)
c = ~a
print ('=============NOT============')
print ('    int:',a,',binary:',format(a,'08b'))
print ('-----------------------------(~)') # operation NOT 
print ('    int:',c,',binary:',format(c,'08b'))
d = 0b00001001 # is int 9
e = 0b11111111 # is XOR from 9
print ('    int:',e^d,',binary:',format(e^d,'08b'))

# Shifting for (shift right(>>))
print ('=============Shift Right============')
x1 = a >> 1
x2 = a >> 2
x3 = a >> 3
print ('    int:',a,',binary:',format(a,'08b'))
print ('  shift: 1',',binary:',format(x1,'08b'))
print ('  shift: 2',',binary:',format(x2,'08b'))
print ('  shift: 3',',binary:',format(x3,'08b'))

# Shifting for (shift left(>>))
print ('=============Shift Left============')
x1 = a << 1
x2 = a << 2
x3 = a << 3
print ('    int:',a,',binary:',format(a,'08b'))
print ('  shift: 1',',binary:',format(x1,'08b'))
print ('  shift: 2',',binary:',format(x2,'08b'))
print ('  shift: 3',',binary:',format(x3,'08b'))


  
