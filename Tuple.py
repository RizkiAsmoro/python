'''
TUPLE
->used to store multiple items in a single variable
->ordered, unchangeable and allow dublicate values
->can't update list in tuple
->write using roung brackets ()
'''
members=("ace","bartolomeu","chifon","dracule","ace","kizaru")
print("->members :\n",members,type(members))

member=("ace",)#using coma to devine as tuple
print("->",member,type(member))
member=tuple("ace")#using tuple() to devine as tuple 
print("->",member,type(member))

#convert tuple into list to change
member=("ace",)
a = list(member)
a[0] = "sabo"
member = tuple(a)
print("->how to change tuple:",member)

#convert tuple into list to append
a=("luffy",)
b=list(a)
b.append("sabo")
a=tuple(b)
print("->how to append tuple:",a)

#convert tuple into list to remove
a=("luffy","sabo","ace")
b=list(a)
b.remove("ace")
a=tuple(b)
print("->how to remove tuple :",a)


