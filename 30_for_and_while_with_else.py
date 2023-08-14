'''
Python allows the else keyword to be used with the for and while loops too. 
The else block appears after the body of the loop. 
The statements in the else block will be executed after all iterations are completed. 
The program exits the loop only after the else block is executed.
'''
'''
Syntax:
for counter in sequence:
    #Statements inside for loop block
else:
    #Statements inside else block
'''
for x in range(5):
    print ("iteration no {} in for loop".format(x+1))
else:
    print ("else block in loop")
print ("Out of loop")

# while loop with else:
x = 5
while (x >= 1):
    print(f"Value of x is {x}")
    x -= 1
else:
    print('Statements of else')
print('Out of loop')
print('\n')
# So when break is used then else statemnet will not be executed.
x = 5
while (x >= 1):
    print(f"Value of x is {x}")
    x -= 1
    if x == 0:
        break
else:
    print('Statements of else')
print('Out of loop')

for x in range(5):
    print("iteration no {} in for loop".format(x+1))
    if x == 4:
        break
else:
    print ("else block in loop")
print ("Out of loop")


