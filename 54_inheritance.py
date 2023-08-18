'''
Inheritance in python
When a class derives from another class. The child class will inherit all the public and protected properties and methods 
from the parent class. In addition, it can have its own properties and methods,this is called as inheritance.
Python Inheritance Syntax
class BaseClass:
  Body of base class
class DerivedClass(BaseClass):
  Body of derived class
Derived class inherits features from the base class where new features can be added to it. This results in re-usability 
of code.
'''
'''
Types of inheritance:
1. Single inheritance
2. Multiple inheritance
3. Multilevel inheritance
4. Hierarchical Inheritance
5. Hybrid Inheritance
'''
'''
Single Inheritance:
Single inheritance enables a derived class to inherit properties from a single parent class, thus enabling code 
reusability and the addition of new features to existing code.
'''
class Parent:
    def func1(self):
        print("This function is in parent class.")
 
class Child(Parent):
    def func2(self):
        print("This function is in child class.")
 
object = Child()
object.func1()
object.func2()
print("\n")
'''
Multiple Inheritance:
When a class can be derived from more than one base class this type of inheritance is called multiple inheritances. 
In multiple inheritances, all the features of the base classes are inherited into the derived class.
'''
class Mother:
    mothername = ""
 
    def mother(self):
        print(self.mothername)
 
 
class Father:
    fathername = ""
 
    def father(self):
        print(self.fathername)
 
 
class Son(Mother, Father):
    def parents(self):
        print("Father name is :", self.fathername)
        print("Mother name is :", self.mothername)
s1 = Son()
s1.fathername = "Vinod"
s1.mothername = "Surekha"
s1.parents()
print("\n")
'''
Multilevel Inheritance :
In multilevel inheritance, features of the base class and the derived class are further inherited into the new derived 
class. This is similar to a relationship representing a child and a grandfather.
'''
class Grandfather:
 
    def __init__(self, grandfathername):
        self.grandfathername = grandfathername
 
 
class Father(Grandfather):
    def __init__(self, fathername, grandfathername):
        self.fathername = fathername
        Grandfather.__init__(self, grandfathername)
class Son(Father):
    def __init__(self, sonname, fathername, grandfathername):
        self.sonname = sonname
        Father.__init__(self, fathername, grandfathername)
 
    def print_name(self):
        print('Grandfather name :', self.grandfathername)
        print("Father name :", self.fathername)
        print("Son name :", self.sonname)
s1 = Son('Prince', 'Rampal', 'Lal mani')
print(s1.grandfathername)
print(s1.fathername)
print(s1.sonname)
s1.print_name()
print("\n")
'''
Hierarchical Inheritance:
When more than one derived class are created from a single base this type of inheritance is called hierarchical 
inheritance. In this program, we have a parent (base) class and two child (derived) classes.
'''
class Parent:
    def func1(self):
        print("This function is in parent class.")

class Child1(Parent):
    def func2(self):
        print("This function is in child 1.")
      
class Child2(Parent):
    def func3(self):
        print("This function is in child 2.")
 
object1 = Child1()
object2 = Child2()
object1.func1()
object1.func2()
object2.func1()
object2.func3()
print("\n")
'''
Hybrid Inheritance:
Inheritance consisting of multiple types of inheritance is called hybrid inheritance.
'''
class School:
    def func1(self):
        print("This function is in school.")
 
 
class Student1(School):
    def func2(self):
        print("This function is in student 1. ")
 
 
class Student2(School):
    def func3(self):
        print("This function is in student 2.")
 
 
class Student3(Student1, School):
    def func4(self):
        print("This function is in student 3.")
 
object = Student3()
object.func1()
object.func2()