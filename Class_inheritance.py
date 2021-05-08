'''
CLASS INHERITANCE
-Inheritance allows us to define a class that inherits all the methods and properties from another class.
-Parent class is the class being inherited from, also called base class.
-Child class is the class that inherits from another class, also called derived class.
'''
#sampe1
print("==============Sample 1==============")
class Parent():
    def __init__(self,name,age,addres):
        self.name = name
        self.age = age
        self.addres = addres
    def check (self):
        print("name :",self.name,"\nage:",self.age,"\naddres:",self.addres)

class Child(Parent): #inheritance (all the object owned by Parent, owned by chid too)
    pass

jaka = Parent("Jaka",21,"Jakarta")
kaka = Child("kaka", 22, "Bandung")
jaka.check()
kaka.check()

#sampe2 (overwrite)
print("==============Sample 2==============")
class Parent():
    def __init__(self,name,age,addres):
        self.name = name
        self.age = age
        self.addres = addres
    def check (self):
        print("name :",self.name,"\nage:",self.age,"\naddres:",self.addres)

class Child(Parent): #inheritance (all the object owned by Parent, owned by chid too)
    def check(self):
        print("-object in parent has been overwritten")

jaka = Parent("Jaka",21,"Jakarta")
kaka = Child("kaka", 22, "Bandung")

jaka.check()
kaka.check()