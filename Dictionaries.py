'''
DICTIONARIES
->Used to store data values in key (value pairs)
->Dictionaries are ordered, changeable but doesn't allow dublicates
->ca be any data type
'''
data1 = {
    "brand" : "Nike",
    "model" : "running",
    "size" : 42
}
print("->data1 :",data1)
print("->how many items in data1 :", len(data1))

print("================ACCESSING=================")
#Access item in dictionaries
# using []
data1 = {
    "brand" : "Nike",
    "model" : "running",
    "size" : 42
}
x = data1["brand"]
print("->access items brand:", x)

print("================GET KEYS=================")
#.get()
x = data1.get("model")
print("->access items model:", x)

print("================GET VALUES=================")
#Get values()
data1 = {
    "brand" : "Nike",
    "model" : "running",
    "size" : 42
}
x = data1.values()
print("->value of data1 :",x)
data1 ["collor"] = "blue"
print("->add values:",x)

print("================GET ITEMS=================")
#the items() method will return each item in dictionary, as tuples in a list
data1 = {
    "brand" : "Nike",
    "model" : "running",
    "size" : 42
}
x = data1.items()
print("->items of data1 :",x)
data1 ["brand"] = "adidas"
print("->change items :",x)

print("================CHANGE=================")
#change values
data1 = {
    "brand" : "Nike",
    "model" : "running",
    "size" : 42
}
data1["model"] = "sport"
data1.update({"size" : 41}) #using method .update()
print("->after data changed :",data1)