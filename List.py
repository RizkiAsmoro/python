'''
LIST
-used to store multiple items in a single variable
-List are create using square brackets
-List are allow duplicates
'''

#List are defined as objects with the data type 'list' -> <class 'list'>
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

