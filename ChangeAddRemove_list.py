'''
Change, Add and Remove of List
'''

crew = ["nami","robin","hancock","reiju","monet"]
print("->Main List :\n",crew)

print("===================CHANGE==================")
#change specify item list
crew = ["nami","robin","hancock","reiju","monet"]
crew[2] = "stussy"
print("->change list 2:\n",crew)
#change and insert range item list values
#sample 1 
crew = ["nami","robin","hancock","reiju","monet"]
crew[1:3] = ["stussy","shirahoshi"]#refer range of index and define new values
print("->change item range 1-3:\n",crew)
#sample 2 (if we define item more than we replace)
crew = ["nami","robin","hancock","reiju","monet"]
crew[1:2] = ["stussy","shirahoshi"]#new values item will be insert specify, remaining list will be shifted
print("->change item range 1-2:\n",crew)
#sample 3 (if we define item less than we replace)
crew = ["nami","robin","hancock","reiju","monet"]
crew[1:3] = ["stussy"]#new values item will be insert specify, remaining list in specify range will remove
print("->change item range 1-2:\n",crew)
#Sample 4 (insert). Insert new item list without replacing any of existing list
crew = ["nami","robin","hancock","reiju","monet"]
crew.insert(2,"shirahoshi") 
print("insert to index 2 :",crew)

print("===================ADD==================")


