# We can find the length of a string using len() function.
fruit = "Mango"
len1 = len(fruit)
print("Mango is a", len1, "letter word.")
'''
A string is essentially a sequence of characters also called an array. Thus we can access the elements of this array.
'''
pie = "ApplePie"
print(pie)
print(len(pie),'\n')
print(pie[:5]) # returns character from start i.e.index 0 upto 4 not including 5.
print(pie[6])	# returns character at specified index 

print(pie[:5])      #Slicing from Start (index 0 to 4)
print(pie[5:])      #Slicing till End (index 5 to last)
print(pie[2:6])     #Slicing in between (index 2 to 5)
print(pie[-8:])     #Slicing using negative index (Here -8 van aslo be written len(pie) - 8 i.e. index 0 till the end)

print(pie[len(pie)-8:])
print(pie[0:])
