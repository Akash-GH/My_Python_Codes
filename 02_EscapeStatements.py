'''
Ctrl + forwardslash(\) to convert a line into comment or viceversa.
\n = newline
\t = tab
\'text\' = adding quotes to a text For eg.'text'
'''
#This is a 'Single-Line Comment'
print("This is a print statement.")
print("Hello World !!!") #Printing Hello World
print("Python Program")
#print("Python Program")
#It will execute a block of code if a specified condition is true.
#If the condition is false then it will execute another block of code.
p = 7
if (p > 5):
    print("p is greater than 5.")
else:
    print("p is not greater than 5.")

print("This will \"execute\"")
'''
Syntax of print function:
print(object(s), sep=separator, end=end, file=file, flush=flush)
'''
print('My name is Akash and I am',21,'years old.',sep = '-',end = 'Nice')
print('\n')
'''
Printing a poem using escape sequence
'''
print("""\'Simple Plan\'\nSimple Sam was a simple man.\nHe lived each day by a simple plan.\nEnjoy your life and live while you can.\nMake each day count and take a stand.
    \nStand on the left or stand on the right,\nWhichever one you think is right.\nLive each day as if your last.\nLife’s too short and gone too fast.\n By Irwin Mercer""")