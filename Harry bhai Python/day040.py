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
Sometimes we may need to pass more arguments than those defined in the actual function. This can be done using 
variable-length arguments.

There are two ways to achieve this:

• Arbitrary Arguments:
• Keyword Arbitrary Arguments:

"""

def average (* numbers):
    sum = 0
    for i in numbers :
        sum = sum+i
    print ("Average is", sum/len(numbers))

average (5,6)                # 5.5
average(1,4,5,6,78,5,4,3)    # 13.25

"""

Arbitrary Arguments:
While creating a function, pass a * before the parameter name while defining the function. The function 
accesses the arguments by processing them in the form of tuple.

"""
# Example:

def name(*name):
    print("Hello,", name[0], name[1], name[2])
name("James", "Buchanan", "Barnes")  # Hello, James Buchanan Barnes