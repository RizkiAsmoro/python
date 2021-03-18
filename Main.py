# Comment
"""Notes : Untuk memindahkan baris code keatas atau kebawah dapat dilakukan dengan 
meletakan kursor paling kiri baris code lalu 
menekan tombol ALT + arah atas atau bawah"""

"""Notes : untuk melakukan copy pada suatu baris code dapat dilakukan dengan
meletakan kursor paling kiri baris code lalu tekan ALT + SIFT + arah bawah/atas"""

# jenis-jenis tipe data
data_integer = 1234567890 #angka tanpa koma
data_float = 13.7 #angka dengan koma
data_string = "rizkiasmoro@gmail.com" #huruf atau simbol, jika ada angka maka angka tsb dikenali sebagai string bukan integer
data_boolean = True #tipe data biner true atau false (boolean)
data_complex = complex(5,6) #bilangan kompleks

#import tipe data dari C untuk menggunakan tipe data dari bahasa C. misal c_double
from ctypes import c_double
data_c_double = c_double(10.8)
print ("Belajar mengenal tipe data")
print ("data :",data_integer,"bertipe data",type (data_integer))
print ("data :",data_float,"bertipe data",type (data_float))
print ("data :",data_string,"bertipe data",type (data_string))
print ("data :",data_boolean,"bertipe data",type(data_boolean))
print ("data :",data_complex,"bertipe data",type (data_complex))
print ("data :",data_c_double,"bertipe data",type (data_c_double))

