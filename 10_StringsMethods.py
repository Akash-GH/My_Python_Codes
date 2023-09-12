'''
Python provides a set of built-in methods that we can use to alter and modify the strings.
'''
# The upper() method converts a string to upper case.
str1 = "AbcDEfghIJklmnopqRstUvwxyz"
print(str1.upper())
print('\n')

# The lower() method converts a string to lower case.
print(str1.lower())
print('\n')

# The strip() method removes any white spaces before and after the string.
str2 = " Silver Spoon "
print(str2.strip())
print('\n')

# the rstrip() removes any trailing characters.
str3 = "Hello !!!"
print(str3.rstrip("!"))
# Note: rstrip will only remove trailing characters after the word not before the word
word = '!!!NAMASKAR!!!'
print(word.rstrip('!'))
print('\n')

# The replace() method replaces all occurences of a string with another string.
print(str2.replace("Sp", "M"))
print('\n')

# The split() method splits the given string at the specified instance and returns the separated strings as list items.
name = 'Akash Narayan Mishra'
print(name.split(" ")) #Splits the string at the whitespace " ".
print('\n')

# The capitalize() method turns only the first character of the string to uppercase and the rest other characters of the string are turned to lowercase. The string has no effect if the first character is already uppercase.
sent = 'my dog loves me.'
print(sent.capitalize())
print('\n')

# The center() method aligns the string to the center as per the parameters given by the user.
message = "Welcome to the Console!!!"
print(len(message))
print(message.center(50))
print(len(message.center(50)))

# We can also provide padding character. It will fill the rest of the fill characters provided by the user.
print(message.center(50, "."))
print('\n')

# The count() method returns the number of times the given value has occurred within the given string.
mantra = "Abracadabra"
print(mantra.count('a'))
print('\n')

# The endswith() method checks if the string ends with a given value. If yes then return True, else return False.
print(message.endswith("!!!"))

# We can even also check for a value in-between the string by providing start and end index positions.
print(message.endswith("to", 4, 10))
print('\n')

#The find() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then return -1.
line = "He's name is Dan. He is an honest man."
print(line.find("is"))
print(line.find("Daniel"))
print('\n')

# The index() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then raise an exception.
print(line.index("Dan"))
# As we can see, this method is somewhat similar to the index() method. The major difference being that index() raises an exception if value is absent whereas find() does not.
#*print(line.index("Daniel"))*#

# The isalnum() method returns True only if the entire string only consists of A-Z, a-z, 0-9. If any other characters or punctuations are present, then it returns False.

agent = 'JamesBond007'
print(agent.isalnum())

# The isalnum() method returns True only if the entire string only consists of A-Z, a-z. If any other characters or punctuations or numbers(0-9) are present, then it returns False.

print(agent.isalpha())
print('\n')

# The islower() method returns True if all the characters in the string are lower case, else it returns False.
greet = 'hello'
print(greet.islower())
print('\n')

# The isprintable() method returns True if all the values within the given string are printable, if not, then return False.
print(agent.isprintable())
print('\n')

# The isspace() method returns True only and only if the string contains white spaces, else returns False.
space = ' ' # using Spacebar
print(space.isspace())
print(agent.isspace())
space2 = '  ' # using tab 
print(space2.isspace())
print('\n')

# The istitile() returns True only if the first letter of each word of the string is capitalized, else it returns False.

who = "World Health Organization" 
print(who.istitle())

bird = "To kill a Mocking bird"
print(bird.istitle())
print('\n')
# The isupper() method returns True if all the characters in the string are upper case, else it returns False.
upperwho =  'WORLD HEALTH ORGANIZATION'
print(upperwho.isupper())

# The startswith() method checks if the string starts with a given value. If yes then return True, else return False.
lang = "Python is a Interpreted Language" 
print(lang.startswith("Python"))

# The swapcase() method changes the character casing of the string. Upper case are converted to lower case and lower case to upper case.

print(lang.swapcase())
print('\n')

# The title() method capitalizes each letter of the word within the string.
print(line.title())

oop = 'object oriented programming.'
print(oop.title())
