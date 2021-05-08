'''
CLASS INHERITANCE
'''

class Parent():
    def __init__(self,name,age,addres):
        self.name = name
        self.age = age
        self.addres = addres
    def check (self):
        print("name :",self.name,"\nage:",self.age,"\naddres:",self.addres)

jaka = Parent("Jaka",21,"Jakarta")
kaka = Parent("kaka", 22, "Bandung")

jaka.check()
kaka.check()