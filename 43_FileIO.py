'''
Opening a File
Before we can perform any operations on a file, we must first open it. Python provides the open() function to open a file.
It takes two arguments: the name of the file and the mode in which the file should be opened. The mode can be 'r' for 
reading, 'w' for writing, or 'a' for appending.
'''
f = open('myfile.txt', 'r')
contents = f.read()
print(contents)
'''
Writing to a File
To write to a file, we first need to open it in write mode.
We can then use the write() method to write to the file.
'''
f = open('myfile.txt', 'w')
f.write('Welcome to my world ')
'''
Keep in mind that writing to a file will overwrite its contents. If you want to append to a file instead of overwriting
it, you can open it in append mode.
'''
f = open('myfile.txt', 'a')
f.write('My name is Akash Mishra')
'''
Closing a File
It is important to close a file after you are done with it. This releases the resources used by the file and allows other
programs to access it.

To close a file, you can use the close() method.
'''
f = open('myfile.txt', 'r')
matter = f.read()
print(matter)
f.close()
'''
The 'with' statement
Alternatively, you can use the with statement to automatically close the file after you are done with it.
'''
with open('myfile.txt', 'r') as f:
    matter = f.read()
    print(matter)
