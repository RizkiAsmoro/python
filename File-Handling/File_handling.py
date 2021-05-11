'''
"w" - Write - Opens a file for writing, creates the file if it does not exist
"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists
"r+"- write and read mode
'''

#write mode
file = open("data.txt","w")
file.write("This is data text, created by python")
file.write("\nthis is 2nd row data text")
file.write("\nthis is 3rd row data text")
file.close() #need close tomakesure data.txt saved in write mode

#read mode
file2 = open("data.txt","r")
#print(file2.read()) # it will read all content data if .read(10) its mean will read 10 character 
print(file2.readline()) # read data by line
file2.close()

#append mode
file3 = open("data.txt","a")
file3.write("\nthis text made using append")
file3.close()

