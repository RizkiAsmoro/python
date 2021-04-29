'''
Variable Scope Global and Local
'''
# Local Variable
name01 = "Jaka"

def changeName(newName):
    name01 = newName
    print("-changing name Jaka tobe :", name01) #it will print the new name (Jack)

changeName("Jack")
print("-now the name is :",name01) # the variable name01 is local variable so if we print here the value not change
print(20*"=")

# Global Variable
number = 10
role = "striker"
def changeNumber(newNumber):
    global number #the value of variable name will changing if we use syntax global
    number = newNumber
    print("-changing the number from 10 tobe :",number)
def changeRole(new02Number,new02Role):
    global number,role
    number = new02Number
    role = new02Role
    print("-changing the role from striker tobe :",role)
    
changeNumber(100)
changeRole(200,"midfielder")
print("-change again the number tobe:", number,"the role is",role) #the value of variable number is changed
