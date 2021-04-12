'''
List
-used to store multiple items in a single variable
-List are create using square brackets
-List are allow duplicates
'''

#List items are indexed start from[0] next[2] and etc
players = ["ronaldo", "messi", "neymar", "mbape", "ronaldo"]
print("This is list of top football players :", players)

#determine how many items in a list
players = ["ronaldo", "messi", "neymar", "mbape", "ronaldo"]
print("Number of items list: ",len(players)) #if there is the same list item it will be counted

#Item list can be any data type and contain different data type
players = ["ronaldo", 7, True]
print(players)

#List are defined as objects with the data type 'list' -> <class 'list'>
players = ["ronaldo", 7, True]
print(type(players))
 
# using list() constructor when creating a new list and can using double round-brackets
players = list(("ronaldo", "messi", "neymar", "mbape", "ronaldo"))
print(players)
