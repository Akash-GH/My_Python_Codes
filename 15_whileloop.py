'''
As the name suggests, while loops execute statements while the condition is True. As soon as the condition becomes False, the interpreter comes out of the while loop.
'''
# Example of while loop:
count = 5
while (count > 0):
  print(count)
  count = count - 1

print('\n')

# Example of else with while loop:
x = 5
while (x > 0):
    print(x)
    x = x - 1
else:
    print('counter is 0')

'''
do..while is a loop in which a set of instructions will execute at least once (irrespective of the condition) and then the repetition of loop's body will depend on the condition passed at the end of the while loop. It is also known as an exit-controlled loop.
'''
#example of dowhile loop;
while True:
  number = int(input("Enter a positive number: "))
  print(number)
  if not number > 0:
    break

while True:
  runs = int(input('Enter the no. of runs: '))
  print(runs)
  if runs > 99:
    print('Century')
    break