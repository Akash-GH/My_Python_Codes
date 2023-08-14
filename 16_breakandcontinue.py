"""
The break statement enables a program to skip over a part of the code. A break statement terminates the very loop it lies within.
"""
# Example of break statement:
for i in range(1,101,1):
    print(i ,end=" ")
    if(i==50):
        break
    else:
        print("Mississippi")
print("Thank you")

num  = int(input('Enter the number: '))
for i in range(12):
  if(i == 10):
    print('Table of given number',num ,'is over')
    break
    print('Table of given number',num ,'is over')
  print(num,"X", i+1, "=", num * (i+1))

"""
The continue statement skips the rest of the loop statements and causes the next iteration to occur.
"""
# Example of continue statement:
for i in [2,3,4,6,8,0]:
    if (i%2!=0):
        continue
    print(i)