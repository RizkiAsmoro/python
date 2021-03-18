# Mempelajari cara mendapatkan nilai dari iput 

# data yang ditampilkan otomatis berupa string
huruf = input ("masukan huruf =")
print (huruf, "tipe ",type(huruf))

# get input integer / float

#angka = int ( input ("masukan angka ="))
angka = float (input ("masukan angka ="))
print (angka, "tipe data",type(angka))


# get input boolean
biner = bool (int(input("masukan biner ="))) #input dicasting ke integer dulu lalu dicasting ke boolean
print (biner, "tipe data",type(biner))

