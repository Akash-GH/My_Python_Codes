'''
Lists are ordered collection of data items.
They store multiple items in a single variable.
List items are separated by commas and enclosed within square brackets [].
Lists are changeable meaning we can alter them after creation.
'''
lst1 = [1,2,2,3,5,4,6]
lst2 = ["Red", "Green", "Blue"]
print(lst1)
print(lst2)

details = ["Abhijeet", 18, "FYBScIT", 9.8]
print(details)
# Indexing
colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [0]      [1]     [2]      [3]      [4] Positive Indexing
#          [-5]     [-4]    [-3]     [-2]     [-1]  Negative Indexing     
print(colors[2])
print(colors[4])
print(colors[0])
print(colors[-1])
print(colors[-3])
print(colors[-5])
if "Yellow" in colors:
    print("Yellow is present.")
else:
    print("Yellow is absent.")
if "Orange" in colors:
    print("Orange is present.")
else:
    print("Orange is absent.")
# Slicing
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[3:7])	#using positive indexes
print(animals[-7:-2])	#using negative indexes'animals[2:7]
print(animals[4:])	#using positive indexes 
print(animals[-4:])	#using negative indexes animals[5:]
print(animals[:6])	#using positive indexes
print(animals[:-3])	#using negative indexes animals[0:6]
print(animals[::2])		#using positive indexes
print(animals[-8:-1:2])	#using negative indexes animals[1:8:2]
'''
List comprehensions are used for creating new lists from other iterables like lists, tuples, dictionaries, sets, and even in arrays and strings.

List = [Expression(item) for item in iterable if Condition]

Expression: It is the item which is being iterated.

Iterable: It can be list, tuples, dictionaries, sets, and even in arrays and strings.

Condition: Condition checks if the item should be added to the new list or not.
'''
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)
namesWithmore4 = [item for item in names if (len(item) > 4)]
print(namesWithmore4)