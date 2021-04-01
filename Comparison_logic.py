'''
Comparison logic  base on input value without 'if else' condition
'''
#OR-codition one of them condition must be true
#+++++++++5---------10+++++++++
'''
a = float(input("\nInput value less than 5 OR greater than 10 :"))
x = a < 5 #compare input value is less than 5 ?
y = a > 10 #compare input value is grater than 10 ?
z = x or y 
print (a,'< 5:',x)
print (a, '> 10:',y)
print ('result x or y :', z)

#AND-slice both condition must be true
#-----------5+++++++++10---------
a = float(input("\nInput value greater than 5 AND less than 10 :"))
x = a > 5 #compare input value is greater than 5 ?
y = a < 10 #compare input value is less than 10 ?
z = x and y 
print (a,'> 5:',x)
print (a, '< 10:',y)
print ('result x and y :', z)
'''

#condition ----2++++5----7++++10----
a = float(input("\nInput value ----2++++5----7++++10----:"))
z = (a>2 and a<5)or(a>7 and a<10)
print ('The value is =',z)
print ('Proof below')
b = a < 10
c = a > 7
d = a > 2
e = a < 5 
x = b and c
y = d and e
z = x or y
print (a,'< 10 =',b)
print (a,'> 7 =',c)
print (a,'> 2 =',d)
print (a,'< 5 =',e)
print (b,'and',c,'=',x,'as (X)')
print (d,'and',e,'=',y,'as (Y)')
print ('x or z =',z,'as (proof)')

# CMIIW