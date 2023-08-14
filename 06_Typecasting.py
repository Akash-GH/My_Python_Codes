'''
The conversion of one data type into the other data type is known as type casting in python 
There are two types of typecasting:
1. Explicit: Done by programmer.
2. Implicit: Done by python intrpreter.
'''
# Explicit Typecasting
a = '16'
b = '24'
print(a+b) # This will conactenate both numbers as they are in string format
# To make them in number format: int() for integer and float() for floating point numbers or decial numbers
print(int(a)+int(b))
# Another Example of Explicit
string = "15"
number = 7
string_number = int(string) #throws an error if the string is not a valid integer
sum= number + string_number
print("The Sum of both the numbers is: ", sum)

# Implicit Typecasting:
x = 88
y = 9.74
print(type(x))
print(type(y))
z = x+y 
print(z)
print(type(z))
'''
Here inorder to prevent data loss intrepreter converted result z in floating point number
'''