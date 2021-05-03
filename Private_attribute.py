'''
Private Attribute in Class
private attribute mean the attribute can't be access out of class
'''
'''##sampe private attribute can't be access
class pirates():
    __age = 90
    def __init__(self):
        print("ages :")
y = pirates()
print(y.__age)
'''##it will be error because in class pirates() has no attribute __age

#how to access private attribute
class students():
    #double underscore
    #only can be access inside class syudents()
    __score = 0  
    def __init__(self,input_name,input_grade):
        self.name = input_name
        self.grade = input_grade
    def midExam (self,midScore):
        self.__score = midScore
    def finalExam (self,finalScore):
        self.__score = finalScore
    def totalScore (self):
        if self.__score <= 60:
            print("you did't pass")
        else:
            print("you passed")

x = students("John", 7)
print("student:",x.name,"grade",x.grade)
x.midExam(20)
x.finalExam(40)
x.totalScore()

