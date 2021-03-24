'''
DATA TYPE
'''

data_integer = 1234567890 #numbers
data_float = 13.7 #numbers with coma
data_string = "rizkiasmoro@gmail.com"
data_boolean = True #value true and false (boolean)
data_complex = complex(5,6) #complex number

#import data type from C to use data type from C like c_double
from ctypes import c_double
data_c_double = c_double(10.8)
print ("Data type introduction")
print ("data :",data_integer,"data type",type (data_integer))
print ("data :",data_float,"data type",type (data_float))
print ("data :",data_string,"data type",type (data_string))
print ("data :",data_boolean,"data type",type(data_boolean))
print ("data :",data_complex,"data type",type (data_complex))
print ("data :",data_c_double,"data type",type (data_c_double))

