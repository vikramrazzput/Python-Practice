# python function arguments

"""

There are four types of arguments that we can provide in a function:

• Default Arguments
• Keyword Arguments
• Variable length Arguments
• Required Arguments

"""

"""

Variable-length arguments:
Sometimes we may need to pass more arguments than those defined in the actual function. This can be done 
using variable-length arguments.

There are two ways to achieve this:

• Arbitrary Arguments:
• Keyword Arbitrary Arguments:

"""


"""

Keyword Arbitrary Arguments:
While creating a function, pass a * before the parameter name while defining the function. The function 
accesses the arguments by processing them in the form of dictionary.

"""
# Example:

def name(**name):
    print("Hello,", name["fname"], name["mname"], name["lname"])
name(mname = "Buchanan", lname = "Barnes", fname = "James")

"""
OUTPUT:
Hello, James Buchanan Barnes
"""

