'''
Stacks : Last-in-First-Out (LIFO) principle
Queues : First-in-First-Out (FIFO) principle
'''
from collections import deque

#Stacks
print(25*"=","STACKS")
numbers = [1,2,3,4,5,6]
print("-list",numbers)

numbers.append(7)
print("-add 7 in list",numbers)

numbers.append(8)
print("-add 8 in list", numbers)

numbers.pop()
print("-Last in - first out",numbers)

#Queues (using library deque)
print(25*"=","QUEUES")
numbers = deque([1,2,3,4,5,6])
print("-list",numbers)

numbers.append(7)
print("-add 7 in list",numbers)

numbers.append(8)
print("-add 8 in list", numbers)

numbers.popleft()
print("-First in - First out",numbers)