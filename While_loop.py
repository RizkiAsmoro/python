'''
While Loop
as long the condition TRUE, the proccess will continue
'''
#While with condition
a = 1
while a < 5:
    print("number ",a)
    a +=1
print("end of WHILE")

print(20*"=")
#While using variable boolean
a = True
b = 1
while a:
    print("number :",b)
    if b is 5:
        a = False
        print("number found",b)
    b +=1

#BREAK
print(20*"=","BREAK")
number = 1
while number < 6:
    if number is 3: 
        print("check 1")
        break # when condition fulfilled, the loopin proccess will ended and go out of loop
    print("number",number)
    number +=1
else:
    print("end of loop")
print("out of loop")

#CONTINUE
print(20*"=","CONTINUE")
x = 1
while x < 6:
    if x is 3: 
        x +=1
        print("check 1")
        continue
    print("number",x)
    x +=1
else:
    print("end of loop")
print("out of loop")

#PASS
print(20*"=","PASS")
number = 1
while number < 6:
    if number is 3: 
        pass 
    print("number",number)
    number +=1
else:
    print("end of loop")
print("out of loop")
