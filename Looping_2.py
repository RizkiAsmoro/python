'''
FOR,Else Loop
Continue, pass
'''
# print range number
for i in range(0,5): 
    print(i)

print(20*"=","range increment")
for i in range (10,30,5): #range 10 to 30, increment 5
    print(i)

# For Else
print(20*"=","for else")
number = 3
for i in range (1,6):
    print(i) # print range number 1 to 5
    if i is number:
        print("number",number," was found")
        break # 'break' to exit from 'if' condition 
else: # 'else' still inside 'for loop' condition
    print("number not found") 


#continue
print(20*"=","continue")
for i in range(1,6):
    if i is 3:
        print(i)
        continue
        print("check number")
    print("current number is ",i)
    if i is 3:
        print("number",3,"was found")
else:
    print("loop ended")

#pass
print(20*"=","pass")
for i in range(1,6):
    if i is 3:
        print("i number is ",i)
        pass
        print("check number")
    print("current number is ",i)
    if i is 3:
        print("number",3,"was found")
else:
    print("loop ended")