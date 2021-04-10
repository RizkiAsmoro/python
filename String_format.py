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

#6
minus_number = -100
plus_number = +200
formatminus = f"->Sample of minus number : {minus_number:+d}"# format minus
formatplus = f"->Sample of plus number : {plus_number:+d}"# format plus
print(formatminus)
print(formatplus)

#7
percentage_num = 0.25
f_percentage = f"-> Format Percentage : {percentage_num:.2%}"
print(f_percentage)

#8
num1 = 120
num2 = 10
arithmetic = f"->Sample arithmetic 120 : 10 = {num1/num2}"
print(arithmetic)

#9
number = 16
f_binary = f"number 16 in binary : {bin(number)}"
f_octal = f"number 16 in octal : {oct(number)}"
f_hexadecimal = f"number 16 in hexadecimal : {hex(number)}"
print(f_binary)
print(f_octal)
print(f_hexadecimal)
