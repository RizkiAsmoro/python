'''
For Loop
'''

#iterable list
fruits = ["mango","durian","pineapple","apple"]
for x in fruits: # x is new varibale and will access each component of fruits
    print(x)
    print(len(x)) # length each of list 

print(20*"=")
#string as iterable
fruits = ["mango","durian","pineapple","apple"]
durian = "durian"
for i in durian:
    print(i)

print(20*"=")
# for inside for
fruits = ["mango","durian","pineapple","apple"]
vegetables = ["carrots","spinach","cabbage","potato"]
cart = [fruits, vegetables]

for subCart in cart: # get list each layer
    print(subCart) # print list 
    for component in subCart: #get each component
        print(component)

