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

print("================ADD=================")
data1 = {
    "brand" : "Nike",
    "model" : "running",
    "size" : 42
}
data1["color"] = "black"
data1.update({"year": 2020}) #using .update()
print("->after adding :",data1)

print("================REMOVE=================")
#.pop()
data1 = {
    "brand" : "Nike",
    "model" : "running",
    "size" : 42,
    "year" : 2020,
    "color" : "black"
}
data1.pop("size") #remove value of "size"
print("->remove size :",data1)
#.popitem()
data1 = {
    "brand" : "Nike",
    "model" : "running",
    "size" : 42,
    "year" : 2020,
    "color" : "black"
}
data1.popitem() #remove the last isert item
print("->remove last inser :",data1)
#del
data1 = {
    "brand" : "Nike",
    "model" : "running",
    "size" : 42,
    "year" : 2020,
}
del data1["year"]
print("-> remove using del:",data1)
#clear (will be clear dictionaries items)
data1 = {
    "brand" : "Nike",
    "model" : "running",
    "size" : 42,
    "year" : 2020,
}
data1.clear()
print("->clear dictionary:",data1)

print("================COPY=================")
'''
can't simply like data1 = data2, because 
data2 will be reference to data1 and,
if data1 list changed then data2 will changed(dependencies)
'''
#.copy()
data1 = {
    "brand" : "Nike",
    "model" : "running",
    "size" : 42,
    "year" : 2020,
}
data2 = data1.copy()
print("->copy from data1 to data2", data2)
#dict()
data1 = {
    "brand" : "Nike",
    "model" : "running",
    "size" : 42,
    "year" : 2020,
}
data2 = dict(data1)
print("->copy using dict()", data2)


print("================NESTED=================")
#sample 1
inventory = {
    "stock1": {
    "brand" : "Nike",
    "model" : "running",
    "size" : 42
    },
    "stock2": {
    "brand" : "Adidas",
    "model" : "sport",
    "size" : 41
    },
}
print("->sample 1",inventory)

#sample 2
stock1 = {
    "brand" : "Nike",
    "model" : "running",
    "size" : 42
    }
stock2 = {
    "brand" : "Adidas",
    "model" : "sport",
    "size" : 41
    }
inventory = {
    "stock1" : stock1,
    "stock2" : stock2
}
print("->stock 1 :",stock1)
print("->stock 2 :",stock2)
