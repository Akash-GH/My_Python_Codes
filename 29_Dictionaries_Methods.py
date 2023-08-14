'''
update()
The update() method updates the value of the key provided to it if the item already exists in the dictionary,
else it creates a new key-value pair.
'''
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)
print('\n')
info.update({'age':20})
info.update({'DOB':2001})
print(info)
print('\n')
# Removing items from dictionary:
'''
clear():
The clear() method removes all the items from the list.
'''
info = {'name':'Karan', 'age':19, 'eligible':True}
info.clear()
print(info)
print('\n')
'''
pop():
The pop() method removes the key-value pair whose key is passed as a parameter.
'''
info = {'name':'Karan', 'age':19, 'eligible':True}
info.pop('eligible')
print(info)
print('\n')
'''
popitem():
The popitem() method removes the last key-value pair from the dictionary.
'''
info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
info.popitem()
print(info)
print('\n')
'''
del:
we can also use the del keyword to remove a dictionary item.
'''
info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
del info['age']
print(info)
print('\n')
'''
If key is not provided, then the del keyword will delete the dictionary entirely.
'''
info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
del info
#print(info)
