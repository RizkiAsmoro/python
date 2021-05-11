'''
"w" - Write  
"r" - Read 
"a" - Append 
"x" - Create 
"r+"- write and read mode
'''

#write mode 'w' - Opens a file for writing, 
#creates the file if it does not exist
file = open("data.txt","w")
file.write("This is data text, created by python")
file.write("\nthis is 2nd row data text")
file.write("\nthis is 3rd row data text")
file.close() #need close tomakesure data.txt saved in write mode

#read mode 'r' - Default value. Opens a file for reading, 
#error if the file does not exist
file2 = open("data.txt","r")
#print(file2.read()) # it will read all content data if .read(10) its mean will read 10 character 
print(file2.readline()) # read data by line
file2.close()

#append mode 'a' - Opens a file for appending, 
#creates the content data if it does not exist
file3 = open("data.txt","a")
file3.write("\nthis text made using append")
file3.close()

#create 'x' - Creates the specified file, 
#file4 = open("data.txt","x") #returns an error if the file exists
file4 = open("data2.txt","x") # 
file4.write("data create by mode create 'x'")
file4.write("\ndelete the data2.txt before running the program")
file4.close()


