'''
Basic Arithmetic base on input
'''
val_a = float(input ('Input value for a ='))
val_b = float(input ('Input value for b ='))
val_c = float(input ('Input value for c ='))


# addition
add_result = val_a + val_b
print (val_a,"+",val_b,"=",add_result)

# subtraction
subtract_result = val_a - val_b
print (val_a,"-",val_b,"=",subtract_result)

# multiplication
multipy_result = val_a * val_b
print (val_a,"*",val_b,"=",multipy_result)

# division
div_result = val_a / val_b
print (val_a,"/",val_b,"=",div_result)

# Eksponent
eks_result = val_a ** val_b
print (val_a,"Eksponent",val_b,"=",eks_result)

# Modulus / remainder of the division
mod_result = val_a % val_b
print (val_a,"modulus",val_b,"=",mod_result)

# Floor division / rounding off the division
fd_result = val_a // val_b
print (val_a,'floor division',val_b,'=',fd_result)

# Precedence (priority)
'''
order of priority
1. ()
2. Eksponen **
3. multiplication, pdivision, modulus, floor division
4. addition & subtraction
'''
preced = val_a ** val_b * val_c + val_a / val_b - val_b % val_c // val_a 
print (val_a,'**',val_b,'*',val_c,'+',val_a,'/',val_b,'-',val_b,'%',val_c,'//',val_a,'=',preced)  


