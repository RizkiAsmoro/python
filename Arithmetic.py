# Aritmatika sederhana dengan menggunakan inmput 
'''
val_a = 10
val_b = 3
val_c = 5
'''
val_a = float(input ('masukan nilai a ='))
val_b = float(input ('masukan nilai b ='))
val_c = float(input ('masukan nilai c ='))


# Penjumlahan
jumlah = val_a + val_b
print (val_a,"+",val_b,"=",jumlah)

# Pengurangan
kurang = val_a - val_b
print (val_a,"-",val_b,"=",kurang)

# Perkalian
kali = val_a * val_b
print (val_a,"*",val_b,"=",kali)

# Pembagian
bagi = val_a / val_b
print (val_a,"/",val_b,"=",bagi)

# Eksponen
pangkat = val_a ** val_b
print (val_a,"pangkat",val_b,"=",pangkat)

# Modulus / sisa pembagian
mod = val_a % val_b
print (val_a,"modulus",val_b,"=",mod)

# Floor division (pembulatan hasil pembagian)
fd = val_a // val_b
print (val_a,'floor division',val_b,'=',fd)

# Precedence (prioritas)
'''
Urutan prioritas
1. ()
2. Eksponen **
3. Perkalian, pembagian, modulus, floor division
4. Penjumlahan & pengurangan
'''
preced = val_a ** val_b * val_c + val_a / val_b - val_b % val_c // val_a 
print (val_a,'**',val_b,'*',val_c,'+',val_a,'/',val_b,'-',val_b,'%',val_c,'//',val_a,'=',preced)  


