'''
LIST
-used to store multiple items in a single variable
-List are create using square brackets
-List are allow duplicates
'''

#List are defined as objects with the data type 'list' -> <class 'list'>
#this is how to access list
players = ["ronaldo", "messi", "neymar", "mbape", "ronaldo", "haland"]
print("This is list of top football players :\n",players, (type(players)))
print("->Number of items : ",len(players))#determine how many items in a list, if there is the same list item it will be counted
print("->Index 0 :",players[0])#List temsarange start from the first list to 4
print("->Index -1 :",players[-1])#Negative indexing means start from the end of list
print("->Index 1 to 4 :",players[1:4])#Specify a range of index, last spicify index list not included
print("->Index to 3 :",players[:3])#range start from the first list to 3, last spicify index list not included
print("->Index from 3 :",players[3:])#range start from the list 3 to the last
print("->range from -4 to -1 :",players[-4:-1])#list -1 not included


#Item list can be any data type and contain different data type
players = ["ronaldo", 7, True]
print("->List can be any data type:",players)

# using list() constructor when creating a new list and can using double round-brackets
players = list(("ronaldo", "messi", "neymar", "mbape", "ronaldo", "haland"))
print("->",players)

print("=================SORT=================")
#Sort() to sort alphanumerically & ascending by default
players = ["ronaldo", "messi", "neymar", "mbape", "ronaldo", "haland"]
players_no = [7,10,11,9,7,13]
players.sort()#sort by ascending
players_no.sort()
print(players) 
print(players_no)
#sort descending
players.sort(reverse=True)
players_no.sort(reverse=True)
print(players) 
print(players_no)
#case sensitive sort
players = ["Ronaldo", "messi", "neymar", "mbape", "haland"]
players.sort()#starting from that beginning with capital
print(players)
players = ["Ronaldo", "messi", "neymar", "mbape", "haland"]
players.sort(key=str.lower)#lowercase came first
print(players)
#reverse() to reverse item list
players = ["Ronaldo", "messi", "neymar", "mbape", "haland"]
players.reverse()
print(players)
#sort the list based on how close the number is to 9
def myfunc(n):
    return abs(n - 9) #count the difference
players_no = [7,10,11,9,7,13]
players_no.sort(key = myfunc)
print(players_no)

print("=================COPY=================")
'''
can't simply like data1 = data2, because data2 will be reference to data1 
and, if data1 list changed then data2 will changed(dependencies)
'''
data1 = ["luffy", "zoro", "sanji", "usop"]
crew1 = data1.copy() #using method copy()
print(crew1)

data2 = ["franky", "jimbei", "chopper"]
crew2 = list(data2)# using method list()
print(crew2)

print("=================JOIN=================")
#using operator +
data1 = ["luffy", "zoro", "sanji", "usop"]
data2 = ["franky", "jimbei", "chopper"]
data3 = data1 + data2
print("data1 + data 2 =\n",data3)
#using append
data1 = ["luffy", "zoro", "sanji", "usop"]
data2 = ["franky", "jimbei", "chopper"]
for x in data2:
    data1.append(x)
print("data1 append data2 =\n",data1)
#using extend()
data1 = ["luffy", "zoro", "sanji", "usop"]
data2 = ["franky", "jimbei", "chopper"]
data1.extend(data2)
print(data1)