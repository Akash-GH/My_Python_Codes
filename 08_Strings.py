'''
In python, anything that you enclose between single or double quotation marks is considered a string.
A string is essentially a sequence or array of textual data. Strings are used when working with Unicode characters.
'''
firstname = 'Akash '
lastname = 'Mishra'
print(firstname + lastname)
print('\n')
fullname = firstname + lastname
print('Good Morning! Everyone, My name is', fullname)
print('\n')
print("He said, \'My favourite sports is Cricket and my favourite programming language is Python.\'")

print('\n')
print('''The best quotes contain messages that provide wisdom we can carry with us every day and inspire us to be our best selves. 
Let these words fill you with hope and give you the motivation to keep going, even when things are hard.''')
print('\n')

favouriteSports = 'Cricket'
favouriteLanguage = 'Python'
print(favouriteSports)
print(favouriteLanguage)

# indexing
'''
In most programming language index of a character,list ,tuples, etc starts 
from 0 and end upto the last of that particualr object.
'''

print(favouriteSports[0])
print(favouriteSports[1])
print(favouriteSports[2])
print(favouriteSports[3])
print(favouriteSports[4])
print(favouriteSports[5])
print(favouriteSports[6],'\n')

print(favouriteLanguage[0])
print(favouriteLanguage[1])
print(favouriteLanguage[2])
print(favouriteLanguage[3])
print(favouriteLanguage[4])
print(favouriteLanguage[5])

# The above can be done by suing for loop inorder to make code use less space
print('\n')
print('Using For Loop:')
for letter in favouriteSports:
  print(letter)

print('\n')

for letter in favouriteLanguage:
  print(letter)