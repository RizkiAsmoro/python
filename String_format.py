'''
Format in String
'''

# Format sring in string
crew = "Nico Robin"
format_string = f"->Luffy pirates crew {crew} had black hair"
print(format_string)

# Format string in boolean 
boolean = True
format_string = f"->My boolean value is {boolean}"
print(format_string)

# Format string in number
# 1
weigh = 75
format_string = f"->My body weigh is {weigh}Kg"
print(format_string)
#2
num_int = 123
format_string = f"->This is interger {num_int}"
print(format_string)
#3
num_int = 10000
format_string = f"->Order numbers by thousands {num_int:,}"
print(format_string)
#4
num_int = 12312.765543
format_string = f"->Decimal {num_int:.3f}" # get 3 digits behind dot
print(format_string)
#5
num = 12312.765543
format1 = f"->Leading zero :{num:8.2f}" 
# get 8 character from front and get 2 digit behind dot 
# (total character 8)
format2 = f"->Leading zero :{num:11.2f}" 
# it will display 3 character empty space and get 8 character from front and get 2 digit behind dot 
# (total character 11)
print(format1)
print(format2)
