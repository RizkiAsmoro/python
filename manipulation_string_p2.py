'''
String Manipulation Part 2
'''

#lowercase and uppercase
f_name = "Monkey D Luffy"
print ("normal :" + f_name)
uper = f_name.upper() # change object tobe upercase
lower = f_name.lower() # change object tobe upercase
print ("uper :" + uper)
print ("lower :" + lower)

#'is' for check component uppercase / lowercase
'''
isalpha()   --> to check the object are only alphabet
isalnum()   --> to check the object are numbers and alphabet
isdecimal() --> to check the object are only numbers
isspace()   --> to check the object are space, tab, newline
istitle()   --> to check every word beginning with a capital letter
'''
text = "marco"
title = "One Piece : Strong World"
lower_check = text.islower()
upper_check = text.isupper()
title_check = title.istitle()
print (text + " is lowercase :" + str(lower_check))
print (text + " is uppercase :" + str(upper_check))
print (title + " -> is title : " + str(title_check))

# using startswith() and endswith() to check component
start = ("Nico Robin").startswith("Nico") # component must be exacly same the uppercase, lowercase, etc
end = ("Nico Robin").endswith("Robin")
print ("'Nico Robin' start with " + "Nico :" + str(start))
print ("'Nico Robin' end with " + "Robin :" + str(end))

# join() and split() component
text2 = ["man","with","a","mission"]
text3 = "game-of-thrones"
jointext  = " ".join(text2) #join and separate with space
print (jointext)
print (text3.split("-"))

# rjust(), ljust(), center() strip()
right = "Borobudur".rjust(15)
left = "Borobudur".ljust(15)
middle = "Borobudur".center(15,"+")
cut_right = right.strip(" ")
cut_left = left.strip(" ")
cut_middle = middle.strip("+")
print ("'" + right + "'") # right align 15 character
print ("'" + left + "'") # left align 15 character
print ("'" + middle + "'") # center align 15 character, separate by +
print ("'" + cut_right + "'") # cut the space from the right 
print ("'" + cut_left + "'") # cut the space from the left statement
print ("'" + cut_middle + "'") # cut the + from statement '+++Borobudur+++'

