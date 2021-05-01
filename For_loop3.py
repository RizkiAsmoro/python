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
         'dortmund',
         'PSG',
         'bayern munic',
         'real madrid']


#indexing using enumerate
for i, name in enumerate(players):
    print(i, name) # indexing start from 0