'''
SETS
-> Used to store multiple item in single variable
-> unordered and unidexed (the items will appear in a random order)
-> the items in the sets do not have a defined order
-> We can't be sure in which order item will be appear
-> unchangeable
-> dublicate not allowed
-> 
'''

#using curly brackets
cities = {"jakarta","bandung","surabaya"}
print("->sets of cities :",cities)
print("->length of set :",len(cities)) #length of sets

#can be any data type
sets1 = {"jakarta",22,True}
print("->data type :",(sets1))

#using set()
cities = set(("jakarta","bandung","surabaya"))
print("->constructor set():",cities)

print("===========ACCESS===========")
#Access items sets using for in
cities = set(("jakarta","bandung","surabaya"))
for x in cities:
    print("->",x)

#access specify item in sets
cities = set(("jakarta","bandung","surabaya"))
print("jakarta" in cities)
print("malang" in cities)
print("jakarta","malang" in cities)

print("===========ADD===========")
#can't be change but posible to add new items
#add()
cities = {"jakarta","bandung","surabaya"}
cities.add("malang")
print("->add :",cities)
#update() -  can be iterable object : tuples, list, dictionary etc
cities = {"jakarta","bandung","surabaya"}
cities2 = {"solo","jayapura"}
cities.update(cities2)
print("->update :",cities)

print("===========REMOVE===========")
#remove(), discard(),clear(), del() and pop()
cities = {"jakarta","bandung","surabaya"}
cities.remove("bandung") #also posible using discard()
print("remove :",cities)

cities = {"jakarta","bandung","surabaya"}
cities.clear() #to empties the set or using del() to delete the set completely
print("clear :",cities)

cities = {"jakarta","bandung","surabaya"}
cities.pop() #remove the last item, sets are unordered so it can be random remove item
print(cities)

print("===========JOIN===========")
# using union() - exclude any dublicate item
cities = {"jakarta","bandung","surabaya"}
a = {2,4}
x = cities.union(a)
print("->union :",x)
#using update() - exclude any dublicate item
cities = {"jakarta","bandung","surabaya"}
a = {2,4}
cities.update(a)
print("->update :",cities)
#using intersection_update() - only the same items (keep teh dublicate)
cities = {"jakarta","bandung","surabaya"}
cities2 = {"manado","bandung","jayapura"}
cities.intersection_update(cities2)
print("->intersection_update :",cities)
#using intersection() - rerturn the new sets, only contain the same items in both sets
cities = {"jakarta","bandung","surabaya"}
cities2 = {"jakarta","bandung","jayapura"}
new = cities.intersection(cities2)
print("->intersection :",new)
#using symetric_difference_update() - keep only items are not exist in both sets
cities = {"jakarta","bandung","surabaya"}
cities2 = {"jakarta","bandung","jayapura"}
cities.symmetric_difference_update(cities2)
print("->keep the differences :",cities)
#using symetric_difference() - rerturn the new sets, only contain items that not exist in both sets
cities = {"jakarta","bandung","surabaya"}
cities2 = {"jakarta","bandung","jayapura"}
x = cities.symmetric_difference(cities2)
print("->return the differences :", x)

