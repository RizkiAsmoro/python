'''
Data type STRING  and how to use it
'''

print('===Data type STRING  and how to use it===')
# using single quote
single = 'Hi, How are you ?' 
print (single,(type(single)))

# using double quote
double = "You are so beautiful" 
print (double,(type(double)))

# made single quote as a string
s1 = "'single quote as a string'"
print (s1,(type(s1)))

# single quote inside other single quote
s2 = 'such a beautiful day isn\'t it ?'
print (s2,(type(s2)))

# backslash as a string
s3 = 'D:\\user\\computer'
print (s3,(type(s3)))

# tab
s4 = 'how to make \ttab'
print (s4,(type(s4)))

# backspace
s5 = 'This is using \bbackspace'
print (s5,(type(s5)))

# new line & how to detect end of line
print('first line \nsecond line') #LF (line feed) use for - unix,macos,linux
print('first line \rsecond line') # CR (carriage return) use for - commodore, acorn
print('first line \r\nsecond line') # CRLF (cariage return line feed) use for - windows

# literal string / raw string
print("D:\\newproject") #\n as a string

# multiline literal string
print("""
Name : Johny
Age  : 27
""") # it will print exactly like we write

# multiline literal string and raw
print(r"""
Name : Johny
addres  : 27\new jersey
portfolio : www.johny.com/newprofile
""") # it will print exactly like we write

