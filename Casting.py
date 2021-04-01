'''
Casting is Change data type
'''
print ("Learning Casting")

# INTEGER
print ("====Change data INTEGER====")
data_int = 9
data_float = float(data_int) # data is rounded down
data_str = str(data_int) # the displayed data will be in the form of a string even though the displayed data will be a number
data_bool = bool(data_int) # will be FALSE if the integer is 0, other than 0 then the value is TRUE

print ("data = ", data_int,"data type",type(data_int))
print ("data = ", data_float,"data type",type(data_float))
print ("data = ", data_str,"data type",type(data_str)) 
print ("data = ", data_bool,"data type", type(data_bool)) 
 
 # FLOAT
print ("====Change data FLOAT====")
data_float = 9.9
data_int = int(data_float)
data_str = str(data_float)
data_bool = bool(data_float)

print ("data = ", data_float,"data type",type(data_float))
print ("data = ", data_int,"data type",type(data_int))
print ("data = ", data_str,"data type",type(data_str)) 
print ("data = ", data_bool,"data type", type(data_bool)) 

# BOOLEAN
print ("====Change data BOOLEAN====")
data_bool = True
data_int = int(data_bool)
data_str = str(data_bool)
data_float = float(data_bool) 

print ("data = ", data_bool,"data type",type(data_bool))
print ("data = ", data_int,"data type",type(data_int))
print ("data = ", data_str,"data type",type(data_str)) 
print ("data = ", data_float,"data type", type(data_float)) 


# STRING
print ("====Change data STRING====")
data_str = "10"
data_int = int(data_str)
data_bool = bool(data_str)
data_float = float(data_str)
print ("data = ", data_str,"data type",type(data_str))
print ("data = ", data_int,"data type",type(data_int))
print ("data = ", data_bool,"data type",type(data_bool)) 
print ("data = ", data_float,"data type", type(data_float)) 

