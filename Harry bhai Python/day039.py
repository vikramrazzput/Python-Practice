# python function arguments

"""

There are four types of arguments that we can provide in a function:

• Default Arguments
• Keyword Arguments
• Variable length Arguments
• Required Arguments

"""

"""

Required arguments:
In case we don’t pass the arguments with a key = value syntax, then it is necessary to pass the arguments in 
the correct positional order and the number of arguments passed should match with actual function definition.

"""

# Example 1: when number of arguments passed does not match to the actual function definition.

def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)
name("Peter", "Quill")

"""
OUTPUT:
name("Peter", "Quill")\
TypeError: name() missing 1 required positional argument: 'lname'
"""

# Example 2: when number of arguments passed matches to the actual function definition.

def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)
name("Peter", "Ego", "Quill")  # Hello, Peter Ego Quill