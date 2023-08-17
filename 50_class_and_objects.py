'''
Python Class and Objects
A class is a blueprint or a template for creating objects, providing initial values for state (member variables or 
attributes), and implementations of behavior (member functions or methods). The user-defined objects are created 
using the class keyword.
'''
# Creating a Class:
class Details:
    name = "Akash"
    age = 21
'''
Creating an Object:
Object is the instance of the class used to access the properties of the class Now lets create an object of the class.
'''
obj1 = Details()

obj1 = Details()
print(obj1.name)
print(obj1.age)

'''
self parameter
The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to 
the class.

It must be provided as the extra parameter inside the method definition.
'''
class Details:
    name = "Akash"
    age = 21
    def desc(self): # here a description function is created with self parameter and a method is created.
        print("My name is", self.name, "and I'm", self.age, "years old.")

obj1 = Details() # object created which has default values
obj1.desc()

obj2 = Details() # object created which has specific values
obj3 = Details() # object created which has specific values

obj2.name = "Rakesh"
obj2.age = 22
obj2.desc()

obj3.name = "Radhika"
obj3.age = 20
obj3.desc()

