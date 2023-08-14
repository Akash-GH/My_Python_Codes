'''
There are four types of arguments that we can provide in a function:

1. Default Arguments
2. Keyword Arguments
3. Variable length Arguments
4. Required Arguments
'''
# Default Arguments: when no value given it will consider default value
def name(fname, mname = "Jhon", lname = "Whatson"):
    print("Hello,", fname, mname, lname)

name("Amy")
# Keyword Arguments: order does not matters
def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name(mname = "Peter", lname = "Wesker", fname = "Jade")
#Requiredl Arguments: if not fill all the parameters error will occur
# def name(fname, mname, lname):
#     print("Hello,", fname, mname, lname)

# name("Peter", "Quill")
#Required Arguments:
def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name("Peter", "Ego", "Quill")
#Variable length Arguments
# Arbitrary Arguments:in form of tuples
def name(*name):
    print("Hello,", name[0], name[1], name[2])

name("James", "Buchanan", "Barnes")

# Keyword Arbitrary Arguments: in form of dictionary 
def name(**name):
    print("Hello,", name["fname"], name["mname"], name["lname"])

name(mname = "Buchanan", lname = "Barnes", fname = "James")
# return statement used to return the value of the expression back to the calling function.
def name(fname, mname, lname): 
    return "Hello, " + fname + " " + mname + " " + lname

print(name("James", "Buchanan", "Barnes"))