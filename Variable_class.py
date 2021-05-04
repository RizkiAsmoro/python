'''
Variable Class
'''

#sample 1
print("================sample 1==============")
class employees():
    
    department = "Finance" #public variable owned by class
    def __init__(self,input_name,input_id): #all who use self. then it belongs to instances/object
        self.name = input_name #public
        self.id = input_id #public

#main program
a = employees("mario", 1001) # a is the istance / object
b = employees("jane",1002)  # b is the istance / object

#employees.department = "System Analyst" #we can change the value of variable department like this 
a.subdept = "System Analyst" # this is variable instances (overwrite)

print(a.department) #original value variabel department
print(a.subdept) #overwrite value department to subdept 
print(employees.department)

#print the dictionary each object
print(a.__dict__) #it will print -> name:mario, id:1001, department:system analyst

#sample 2
print("================sample 2==============")

class student():
    total_student = 0
    def __init__(self,input_sName,input_sID):
        self.sName = input_sName
        self.sID = input_sID
        
        student.total_student +=1

#main program
x = student("benzema", 3001)
y = student("mane", 3002)
print(student.total_student) #it will count sum of student
