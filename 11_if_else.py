a = int(input("Enter your age: "))
print("Your age is:", a)
# Conditional operators
# >, <, >=, <=, ==, !=
print(a>18) # greater than
print(a<18) # lesser than
print(a>=18) # greater than or equal to
print(a<=18) # lesser tahn or equal to
print(a==18) # equal to
print(a!=18,'\n') # not equal to
'''
Sometimes the programmer needs to check the evaluation of certain expression(s), whether the expression(s) evaluate to True or False. 
If the expression evaluates to False, then the program execution follows a different path than it would have if the expression had evaluated to True.
'''

'''
Based on this, the conditional statements are further classified into following types:

1. if
2. if-else
3. if-else-elif
4. nested if-else-elif.
'''
# Example of if statement
cost = 30
budget = 10
if cost > budget:
  print('You cannot buy')
'''
if the expression evaluates True: block of code in if statement is executed.
if the expression evaluates False: block of code in else statement is executed.
'''
# example of if-else statement
if (a > 18):
  print("You can drive")
else:
  print("You cannot drive")

applePrice = 210
budget = 200
if (applePrice <= budget):
    print("Alexa, add 1 kg Apples to the cart.")
else:
    print("Alexa, do not add Apples to the cart.")

# example of if-elif-else statement
# elif statements can be infinite and it depends on user. This statements are in between of if and else statement. When if statement is false then it will go to elif statements after checking these if they are not true then else statement will be executed.
num = int(input("Enter the value of num: "))
if (num < 0):
  print("Number is negative.")
elif (num == 0):
  print("Number is Zero.") 
elif (num == 999):
  print("Number is Special.")
else:
  print("Number is positive.")

print("I am happy now")

# example of nested statements
# Here there will be another if statements in another if statements.
num = 18
if (num < 0):
    print("Number is negative.")
elif (num > 0):
    if (num <= 10):
        print("Number is between 1-10")
    elif (num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")