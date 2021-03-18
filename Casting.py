#casting tipe data yaitu merubah tipe data dari suatu tipe data ke tipe data lainnya
print ("ini belajar casting")

# INTEGER
print ("====Merubah data INTEGER====")
data_int = 9
data_float = float(data_int) # data akan dibulatkan ke bawah
data_str = str(data_int) # data yang ditampilan akan berupa string walaupun yang ditampilkan angka
data_bool = bool(data_int) # akan FALSE jika integer bernilai 0, selain 0 maka nilainya TRUE

print ("data = ", data_int,"bertipe data",type(data_int))
print ("data = ", data_float,"bertipe data",type(data_float))
print ("data = ", data_str,"bertipe data",type(data_str)) 
print ("data = ", data_bool,"bertipe data", type(data_bool)) 
 
 # FLOAT
print ("====Merubah data FLOAT====")
data_float = 9.9
data_int = int(data_float) # data akan dibulatkan ke bawah
data_str = str(data_float) # data yang ditampilan akan berupa string walaupun yang ditampilkan angka
data_bool = bool(data_float) # akan FALSE jika integer bernilai 0, selain 0 maka nilainya TRUE

print ("data = ", data_float,"bertipe data",type(data_float))
print ("data = ", data_int,"bertipe data",type(data_int))
print ("data = ", data_str,"bertipe data",type(data_str)) 
print ("data = ", data_bool,"bertipe data", type(data_bool)) 

# BOOLEAN
print ("====Merubah data BOOLEAN====")
data_bool = True
data_int = int(data_bool) # data akan dibulatkan ke bawah
data_str = str(data_bool) # data yang ditampilan akan berupa string walaupun yang ditampilkan angka
data_float = float(data_bool) # akan FALSE jika integer bernilai 0, selain 0 maka nilainya TRUE

print ("data = ", data_bool,"bertipe data",type(data_bool))
print ("data = ", data_int,"bertipe data",type(data_int))
print ("data = ", data_str,"bertipe data",type(data_str)) 
print ("data = ", data_float,"bertipe data", type(data_float)) 


# STRING
print ("====Merubah data STRING====")
data_str = "10"
data_int = int(data_str) # String harus angka
data_bool = bool(data_str) # bernilai False jika string kosong 
data_float = float(data_str) # String harus angka
print ("data = ", data_str,"bertipe data",type(data_str))
print ("data = ", data_int,"bertipe data",type(data_int))
print ("data = ", data_bool,"bertipe data",type(data_bool)) 
print ("data = ", data_float,"bertipe data", type(data_float)) 

