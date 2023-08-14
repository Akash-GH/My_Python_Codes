'''
Variables are nothing but a container which stores values.
Data Types:
1. Number: [Integer,Float,Complex]
2. String: (Text) '' or ""
3. Boolean: (True or False)
4. Sequence Data:  (Lists: [], Tuples: ())
5. Mapped Data: Dictionaries {}(keyavlues pairs)
''' 
a = 1 # Integer
b = True # Boolean
c = "Akash" # String
d = None # None
e = complex(4,4) # Complex number
f = 99.99 # float
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print('\n')
print('Type of a is ', type(a))
print('Type of b is ', type(b))
print('Type of c is ', type(c))
print('Type of d is ', type(d))
print('Type of e is ', type(e))
print('Type of f is ', type(f))
print('\n')
'''
List and Tuples are same same except lists are mutable while tuples are immutable.
'''
list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]
print(list1)
tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"))
print(tuple1)
dict1 = {"name":"Akash", "age":21, "canVote":True}
print(dict1)
print('\n')
print('Type of list1 is ',type(list1))
print('Type of tuple1 is ',type(tuple1))
print('Type of dict1 is ',type(dict1))