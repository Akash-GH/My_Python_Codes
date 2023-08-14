# In python, we can raise custom errors by using the raise keyword.
salary = int(input("Enter salary amount: "))
if not 2000 < salary < 5000:
    raise ValueError("Not a valid salary")

a = (input('Enter the number 5 to 9 or quit: '))
if (a == 'quit'):
     print("Great Job!")
elif (int(a)<5 or int(a)>9):
    raise ValueError('Enter the correct value.')
else:
    print(a)