'''
Sometimes a programmer wants to execute a group of statements a certain number of times. This can be done using loops.
Based on this loops are further classified into following main types;

1. for loop
2. while loop
'''
'''
for loops can iterate over a sequence of iterable objects in python. Iterating over a sequence is nothing but iterating over strings, lists, tuples, sets and dictionaries.
'''
# Iterating over string:
name = 'Akash'
for i in name:
    print(i, end=", ")
print('\n')
name = 'Akash'
for i in name:
  print(i)
  if (i== 's'):
    print('Good Job')
print('\n')
# Iterating over list:
colors = ["Red", "Green", "Blue", "Yellow"]
for color in colors:
  print(color)
  for letter in color:
    print(letter)
print('\n')
# range(start: number from which it should be started,stop: number before which it should be started, step: rate at which numbers should be incremented or decremented ) 
for k in range(5):
    print(k)
print('\n')
for k in range(4,9):
    print(k)
print('\n')
# Range of odd numbers from 1 to 100:
print('Odd Numbers from 1 to 100:')
for oddnum in range(1,101,2): # Here it is incremented by 2.
  print(oddnum)
print('\n')
# Range of even numbers from 1 to 100:
print('Even Numbers from 1 to 100:')
for evennum in range(2,101,2): # Here it is incremented by 2.
  print(evennum)  
print('\n')
# Ascending order
print('Numbers from 1 to 100 in Ascending Order:')
for a in range(1,101):
  print(a)
print('\n')
# Descending order
print('Numbers from 1 to 100 in Descending Order:')
for d in range(100,0,-1):
  print(d)