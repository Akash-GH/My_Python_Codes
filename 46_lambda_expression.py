'''
In Python, a lambda function is a small anonymous function without a name. It is defined using the lambda keyword and
has the following syntax:

lambda arguments: expression
'''
'''
Lambda functions are often used in situations where a small function is required for a short period of time. They are
commonly used as arguments to higher-order functions, such as map, filter, and reduce.
'''
# Function to double the input
def double(x):
  return x * 2
print(double(5))
# Lambda function to double the input
double_l = lambda x: x * 2
print(double_l(5))
'''
The above lambda function has the same functionality as the double function defined earlier. However, the lambda function
is anonymous, as it does not have a name.

Lambda functions can have multiple arguments, just like regular functions. Here is an example of a lambda function with 
multiple arguments:
'''
# Function to calculate the product of two numbers
def multiply(x, y):
    return x * y

print(multiply(5,6))
# Lambda function to calculate the product of two numbers
multiply_l = lambda x, y: x * y
print(multiply_l(5,6))
'''
Lambda functions can also include multiple statements, but they are limited to a single expression. For example:
'''
# Lambda function to calculate the product of two numbers,
# with additional print statement
products = lambda x, y: print(f'{x} * {y} = {x * y}')
products(5,6)
'''
In the above example, the lambda function includes a print statement, but it is still limited to a single expression.

Lambda functions are often used in conjunction with higher-order functions, such as map, filter, and reduce.
'''