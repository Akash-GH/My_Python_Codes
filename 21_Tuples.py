'''
Tuples are ordered collection of data items. They store multiple items in a single variable. Tuple items are separated by commas and enclosed within round brackets (). Tuples are unchangeable meaning we can not alter them after creation.
'''
tuple1 = (1,2,2,3,5,4,6)
tuple2 = ("Red", "Green", "Blue")
print(tuple1)
print(tuple2)
#Indexing
country = ("Spain", "Italy", "India",)
#            [0]      [1]      [2]
# Positive Indexing
print(country[0])
print(country[1])
print(country[2])
country1 = ("Spain", "Italy", "India", "England", "Germany")
# Negative Indexing
print(country1[-1]) # Similar to print(country[len(country) - 1])
print(country1[-3])
print(country1[-4])
# Check for item
if "Germany" in country1:
    print("Germany is present.")
else:
    print("Germany is absent.")
if "Russia" in country1:
    print("Russia is present.")
else:
    print("Russia is absent.")

# Range of index
# Syntax: Tuple[start : end : jumpIndex]
animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[3:7])     #using positive indexes
print(animals[-7:-2])   #using negative indexes
print(animals[:6])      #using positive indexes
print(animals[:-3])     #using negative indexes
print(animals[::2])     #using positive indexes
print(animals[-8:-1:2]) #using negative indexes
print(animals[1:8:3])