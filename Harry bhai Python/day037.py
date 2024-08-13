# python function arguments

"""

There are four types of arguments that we can provide in a function:

• Default Arguments
• Keyword Arguments
• Variable length Arguments
• Required Arguments

"""

"""

Default arguments:
We can provide a default value while creating a function. This way the function assumes a default value even 
if a value is not provided in the function call for that argument.

"""
def average(a=9,b=1):
    print ("The average is", (a+b)/2)

#  calling the function
average () # 5.0
average (23,56) # 39.5

average (5) # 3.0

average (b=5) # 7.0

def name(fname, mname = "Jhon", lname = "Whatson"):
    print("Hello,", fname, mname, lname)

name("Amy")  # Hello, Amy Jhon Whatson

