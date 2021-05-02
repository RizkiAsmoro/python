'''
Class and Method
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
