'''
dir(), __dict__ and help() methods in python
We must look into dir(), __dict__() and help() attribute/methods in python. They make it easy for us to understand how 
classes resolve various functions and executes code. In Python, there are three built-in functions that are commonly 
used to get information about objects: dir(), dict, and help(). Let's take a look at each of them:
'''
'''
The dir() method
dir(): The dir() function returns a list of all the attributes and methods (including dunder methods) available 
for an object. It is a useful tool for discovering what you can do with an object. Example:
'''
x = [1, 2, 3]
print(dir(x))

'''
The __dict__ attribute
__dict__: The __dict__ attribute returns a dictionary representation of an object's attributes. It is a useful
tool for introspection. Example:
'''
class Person:
  def __init__(self, name, age):
      self.name = name
      self.age = age
      self.version = 1

    
p = Person("John", 30)
print(p.__dict__)
'''
The help() method
help(): The help() function is used to get help documentation for an object, including a description of its
attributes and methods. Example:
'''
print(help(Person))
'''
In conclusion, dir(), dict, and help() are useful built-in functions in Python that can be used to get information 
about objects. They are valuable tools for introspection and discovery.
'''