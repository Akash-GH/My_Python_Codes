'''
The enumerate function is a built-in function in Python that allows you to loop over a sequence 
(such as a list, tuple, or string) and get the index and value of each element in the sequence at the same time.
'''
# Loop over a list and print the index and value of each element
fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits):
    print(index, fruit)
print('\n')
#Changing the start index
# Loop over a list and print the index (starting at 1) and value of each element
fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)
print('\n')
fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits):
    print(f'{index+1}: {fruit}')
print('\n')
# Loop over a tuple and print the index and value of each element
colors = ('red', 'green', 'blue')
for index, color in enumerate(colors):
    print(index, color)
print('\n')
# Loop over a string and print the index and value of each character
s = 'hello'
for index, c in enumerate(s):
    print(index, c)
print('\n')
numlist = [1,2,3,4,5,6,7,8,9,10]
for num in enumerate(numlist):
    print(num)
print('\n')
# Tuple unpacking
numlist = [1,2,3,4,5,6,7,8,9,10]
for index,num in enumerate(numlist):
    print(index,num)
print('\n')
# sum of all numbers from 1 to 10.
sum = 0
print('index  num\tsum')
for index,num in enumerate(numlist):
    sum = sum + num 
    print(f' {index}.\t{num}\t{sum}')