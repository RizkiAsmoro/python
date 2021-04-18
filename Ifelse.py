'''
IF ELIF ELSE Statement
'''

score = float(input("Input your score : ")) #casting data type from string to float
if 90 <= score <= 101:
    print("->Your grade is A ")
elif 80 <= score <= 90:
    print("->your grade is B ")
elif 70 <= score <= 80:
    print("->your grade is C+ ")
elif 60 <= score <= 70:
    print("->your grade is C")
else:
    print("->you didn't pass")

print(50*"=")
name = input("insert name of mugiwara luffy crew : ")
crew = ["luffy","zoro","nami","sanji","usop","coper","robin","franky","brook","jimbei"]
if name in crew:
    print("->",name,"is one of the crew mate")
if name not in crew:
    print("->",name, "is not crew mate")
