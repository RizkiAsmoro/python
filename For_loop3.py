'''
FOR Loop Technique
'''

players = ['ronaldo',
          'messi',
          'haland',
          'neymar',
          'lewandowski',
          'hazard']
clubs = ['juventus',
         'barcelona',
         'borusia dortmund',
         'PSG',
         'bayern munic',
         'real madrid']


#indexing using enumerate
for i, name in enumerate(players):
    print(i, name) # indexing start from 0

# ZIP
# each literacy must be paired sequentially
for x,y in zip(players, clubs):   
    print(x,'from',y)

# SETS
print("="*25,"sorting the SETS")
crews = {"luffy", "zoro", "sanji", "usop","brook","franky", "jimbei", "chopper","nami","robin"}
for x in sorted(crews):
    print(x)

# DICTIONARIES
print("="*25,"DICTIONARIES")
pirates = {"luffy":"captain",
           "usop":"sniper",
           "nami":"navigator",
           "brook":"musician"}
print("---get the keys---")
for y in pirates.keys(): #will get the keys only
    print(y)
print("---get the values---")
for a in pirates.values(): #will get the value only
    print(a)
print("---get the items---")
for i in pirates.items(): #will get the items of the data
    print(i)




