'''
"w" - Write - Opens a file for writing, creates the file if it does not exist
"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists
"r+"- write and read mode
'''

file = open("data.txt","w")
file.write("This is data text, created by python")
file.close()