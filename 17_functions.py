'''
A function is a block of code that performs a specific task whenever it is called. In bigger programs, where we have large amounts of code, it is advisable to create or use existing functions that make the program flow organized and neat.

There are two types of functions:

1. Built-in functions: Already available by intrepreter
2. User-defined functions: Defined by user itself
'''

'''
Built-in functions:
These functions are defined and pre-coded in python. Some examples of built-in functions are as follows:

min(), max(), len(), sum(), type(), range(), dict(), list(), tuple(), set(), print(), etc.
'''
print('Output given using Built-in Functions:')
print('Hello, Akash Mishra')
'''
User-defined functions:
We can create functions to perform specific tasks as per our needs. Such functions are called user-defined functions.

Syntax:
def function_name(parameters):
  pass
  # Code and Statements
'''
# here there is a catch for eg. if you want to print messages of greeting hello to person of different fname and lname. So instead of making changes to given print we can create a user defined function for the same.
# Example:
def name(fname, lname):
    print("Hello,", fname, lname)
print('Output given using User-Defined Functions:')
name("Akash", "Mishra")