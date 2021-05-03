'''
Class and Method
__init__
'''
#CLASS
print("===============CLASS===============")
class crews():
    name = "the name" #atribute

zoro = crews() #zoro is the instance/object
sanji = crews() #sanji is the instance/object

#change default name
zoro.name = "roronoa zoro" 
sanji.name = "kuroasi no sanji"

#print name after changed
print(zoro.name)
print(sanji.name)

#METHOD in CLASS
#method are inside the class, but function are outside the class
print("============METHOD in CLASS============")
#class
class pirates():
    name = "the name"
    #method
    def power(self): #self used to indentify the object
        print(self.name,"are the sword master")
    def power2(self, condition):
        print(self.name,"are the invisible rope", condition)

#main program
mihawk = pirates()
doflamingo = pirates()

mihawk.name = "takanome mihawk"
doflamingo.name = "donqixote doflamingo"

mihawk.power()
doflamingo.power2("and the cruel one")#input the condition


#how to use __init__ in class and method
print("============USE __init__============")

class marine():
    def __init__(self,input_name, input_power): #input argument()
        self.name = input_name #atribute
        self.power = input_power
z = marine("garp","haki") #init will be executed when class marine called
print(z.name,z.power)

'''
how __init__ works:
1. def __init__ will br exceuted when z=marine() is called
2. we can put the argumen like (self,input_name) inside, to fill in self.name = input_name to initialization
3. __init__ will be executed when initialization object
'''