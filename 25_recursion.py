"""
Recursion is the process of defining something in terms of itself.
In Python, we know that a function can call other functions.
It is even possible for the function to call itself. 
These types of construct are termed as recursive functions.
"""
# Factorials for eg. 5! = 5*4*3*2*1
def factorial(n):
  if (n == 0 or n == 1):
    return 1
  else:
    return n * factorial(n - 1)

print(factorial(5))

def factorial(num): 
    if (num == 1 or num == 0):
        return 1
    else:
        return (num * factorial(num - 1)) 
  

num = 7; 
print("Number: ",num)
print("Factorial: ",factorial(num))

# Fibonacci Series. 0 1 1 2 3 5 8 13 ....
def Fibonacci(n):

  if (n<0):
    print("Incorrect input")
  elif (n==0):
    return 0
  elif (n==1 or n==2):
    return 1
  else:
    return Fibonacci(n-1) + Fibonacci(n-2)

print(Fibonacci(6))