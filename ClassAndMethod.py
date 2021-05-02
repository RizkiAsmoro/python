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
print("============METHOD in CLASS============")
class pirates():
    name = "the name"

mihawk = pirates()
doflamingo = pirates()

mihawk.name = "takanome mihawk"
doflamingo.name = "donqixote doflamingo"

print(mihawk.name)
print(doflamingo.name)