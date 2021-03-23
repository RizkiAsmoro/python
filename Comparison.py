'''Perbandingan nilai sederhana menggunakan input'''
#tipe data harus diset float karena jika tidak maka inputan bertipe data string
val_a = float(input ('Masukan nilai a =')) 
val_b = float(input ('Masukan nilai b ='))

samadengan = val_a == val_b
tdksamadengan = val_a != val_b
lebih = val_a > val_b
kurang = val_a < val_b
kurangsama = val_a <= val_b 
lebihsama = val_a >= val_b


print (val_a,'=',val_b,'=',samadengan)
print (val_a,'!=',val_b,'=',tdksamadengan)
print (val_a,'>',val_b,'=',lebih)
print (val_a,'<',val_b,'=',kurang)
print (val_a,'<=',val_b,'=',kurangsama)
print (val_a,'>=',val_b,'=',lebihsama)

#membandingkan menggunakan 'is' dan 'is not'
#is sebagai object identity
#contoh x = 5, maka x adalah object dan 5 adalah literal
#hex adalah penyimpanan object pada memory
#object harus dibandingkan dengan object
#jika object dibandingkan dengan literal maka akan muncul SyntaxWarning
print ('=========Object indentity (is)')
x = 7
y = 9
identityis = x is y
print ('Jika nilai')
print ('Nilai X =',x,'dengan id hex',hex(id(x)))
print ('nilai Y =',y,'dengan id hex',hex(id(y)))
print ('x is y =', identityis)

x = 7
y = 7
identityis = x is y
print ('Jika nilai')
print ('Nilai X =',x,'dengan id hex',hex(id(x)))
print ('nilai Y =',y,'dengan id hex',hex(id(y)))
print ('x is y =', identityis)

print ('=========Object indentity (is not)')
x = 7
y = 9
identityis = x is not y
print ('Jika nilai')
print ('Nilai X =',x,'dengan id hex',hex(id(x)))
print ('nilai Y =',y,'dengan id hex',hex(id(y)))
print ('x is not y =', identityis)

x = 7
y = 7
identityis = x is not y
print ('Jika nilai')
print ('Nilai X =',x,'dengan id hex',hex(id(x)))
print ('nilai Y =',y,'dengan id hex',hex(id(y)))
print ('x is not y =', identityis)