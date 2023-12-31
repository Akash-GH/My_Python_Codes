'''
local and global variables
Before we dive into the differences between local and global variables, let's first recall what a variable is in Python.

A variable is a named location in memory that stores a value. In Python, we can assign values to variables using the
assignment operator =. For example:
'''

x = 5
y = "Hello, World!"

'''
Now, let's talk about local and global variables.

A local variable is a variable that is defined within a function and is only accessible within that function. It is 
created when the function is called and is destroyed when the function returns.

On the other hand, a global variable is a variable that is defined outside of a function and is accessible from within
any function in your code.

Here's an example to help clarify the difference:
'''

a = 10 # global variable

def my_function():
  b = 5 # local variable
  print(b)

my_function()
print(a)
# print(b) # this will cause an error because y is a local variable and is not accessible outside of the function

'''
In this example, we have a global variable a and a local variable b. We can access the value of the global variable a 
from within the function, but we cannot access the value of the local variable b outside of the function.
'''
'''
The global keyword
Now, what if we want to modify a global variable from within a function? This is where the global keyword comes in.

The global keyword is used to declare that a variable is a global variable and should be accessed from the global scope.
Here's an example:
'''

u = 10 # global variable

def my_function():
  global u
  u = 5 # this will change the value of the global variable x
  v = 5 # local variable

my_function()
print(u) # prints 5
# print(v) # this will cause an error because y is a local variable and is not accessible outside of the function

'''
In this example, we used the global keyword to declare that we want to modify the global variable u from within 
the function. As a result, the value of u is changed to 5.

It's important to note that it's generally considered good practice to avoid modifying global variables from 
within functions, as it can lead to unexpected behavior and make your code harder to debug.
'''