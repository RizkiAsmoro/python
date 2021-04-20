'''
FOR,Else Loop
Continue, pass
'''
# print range number
print(20*"=","RANGE")
for i in range(0,5): 
    print(i)

print(20*"=","range increment")
for i in range (10,30,5): #range 10 to 30, increment 5
    print(i)

# For Else
print(20*"=","FOR ELSE")
number = 3
for i in range (1,6):
    print(i) # print range number 1 to 5
    if i is number:
        print("number",number," was found")
        break # 'break' to exit from 'if' condition 
else: # 'else' still inside 'for loop' condition
    print("number not found") 


#BREAK
print(20*"=","BREAK")
for y in range(1,6):
    if y is 2:
        print("number found :",2)
        break # when the number was found, break will ended proccess of loop and out of loop
        print("check")
    print("number",y)
else:
    print("end of loop")
print("out of loop")

#continue
print(20*"=","CONTINUE")
for x in range(1,6):
    if x is 3:
        print("number found",3)
        continue # when the number has been found, continue the looping proccess until end of range then out of loop
        print("check")
    print("number",x)
else:
    print("end of loop")
print("out of loop")

#pass
print(20*"=","PASS")
for z in range(1,6):
    if z is 2:
        print("number found",2)
        pass # when number was found, pass will print check then continue procces until loop proccess ended
        print("check")
    print("number",z)
else:
    print("end of loop")
print("out of loop")
