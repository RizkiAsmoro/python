'''
FOR Loop Else
'''
# print range number
for i in range(0,5): 
    print(i)

print(20*"=")
for i in range (10,30,5): #range 10 to 30, increment 5
    print(i)

#
print(20*"=")
number = int(input("insert number 1 to 5:"))
for i in range (1,6):
    print(i) # print range number 1 to 5
    if i is number:
        print("number",number," was found")
        break # 'break' to exit from 'if' condition 
else: # 'else' still inside 'for loop' condition
    print("number not found") 