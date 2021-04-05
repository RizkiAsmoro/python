'''
Operation and Manipulation String
'''
print ('Operation and Manipulation String')

# Concatenate
first_name = "monkey"
middle_name = "d"
last_name = "luffy"
fulll_name = first_name + " " + middle_name + "'" +  last_name
print (fulll_name)

# Length 
length =  len(fulll_name)
print ("Length of string is :",length)
 
# check availability of string
check ="d"
status = check in fulll_name
print (check, "in", fulll_name, "is", str(status))

# check not availability of string
check ="d"
status = check not in fulll_name
print (check, "not in", fulll_name, "is", str(status))

# Repeat string
print (5*"Luffy")

# Indexing (Start from 0 in front and start from -1 in back)
print ("index 0 = " + fulll_name[0])
print ("index -1 = " + fulll_name[-1])
print ("index 0-5 = " + fulll_name[0:6])# : is until (if using : then the last of string did't fetched)
print ("index 9-13 = " + fulll_name[9:14])
print ("index 0,2,4,6,8,10,12,13 = " + fulll_name[0:13:2]) # 0 to 13 witn increment 2

# item index min, max and ascii code
print ("The smallest is :" + min(fulll_name)) # teh result is space
print ("The biggest is :" + max(fulll_name))

ascii_code = ord(" ") # ord using for get unicode from string
print (("ASCII code for space :") + str(ascii_code))
ascii_code_2 = ord("a") # ord using for get unicode from string
print (("ASCII code for 'a' :") + str(ascii_code_2))
data = 120
print (("Character for ASCII code for 120 :") + chr(data))

# Operator in method
x = "mokey d luffy is pirates of king"
z = x.count("i") #method count in object x, specific string i
print("counting 'i' in " + x + " : " + str(z))