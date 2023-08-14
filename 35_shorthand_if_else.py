'''
If ... Else in One Line
There is also a shorthand syntax for the if-else statement that can be used when the condition being tested is simple and
the code blocks to be executed are short
'''
'''
if condition:
    result = value_if_true
else:
    result = value_if_false
'''
a = 2
b = 330
print("A") if a > b else print("B")
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
a = 330
b = 2
print("A") if a > b else print("=") if a == b else print("B")
num1 = 10
num2 = 20
print(num1-num2) if num1 > num2 else print(num1+num2) if num1<num2 else print('Both are equal.') 
num1 = 10
num2 = 10
print(num1-num2) if num1 > num2 else print(num1+num2) if num1<num2 else print('Both are equal.') 
num1 = 20
num2 = 10
print(num1-num2) if num1 > num2 else print(num1+num2) if num1<num2 else print('Both are equal.') 
'''
Note :
The shorthand syntax can be a convenient way to write simple if-else statements, especially when you want to assign a 
value to a variable based on a condition.However, it's not suitable for more complex situations where you need to execute
multiple statements or perform more complex logic. In those cases, it's best to use the full if-else syntax.
'''