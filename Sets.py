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

#Access items sets using for in
cities = set(("jakarta","bandung","surabaya"))
for x in cities:
    print("->",x)

#access specify item in sets
cities = set(("jakarta","bandung","surabaya"))
print("jakarta" in cities)
print("malang" in cities)
print("jakarta","malang" in cities)

#can't be change but posible to add

