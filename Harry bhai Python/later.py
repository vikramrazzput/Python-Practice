
# Local Vs Global Variables
"""
Variables may be either global or local:

 - Variables that are defined inside a function body have a local scope, and those defined outside have a global scope. 

 - This means that local variables can be accessed only inside the function in which they are declared, whereas global variables can be accessed throughout the program body by all functions.
"""   
### The global Keyword:
"""
We only need to use the  **global keyword**  in a function if we want to assign or change the global variable instead of creating a local variable. 
global is not needed for printing and accessing. 
Python “assumes” that we want a local variable due to the assignment to a variable inside of a function. Any variable which is changed or created inside of a function is local if it hasn’t been declared as a global variable. To tell Python, that we want to use the global variable, we have to use the keyword  **global**, as can be seen in the following example:
"""

a = 1

# Uses global because there is no local 'a'
def f():
	print('Inside f() : ', a)

# Variable 'a' is redefined as a local
def g():
	a = 2
	print('Inside g() : ', a)

# Uses global keyword to modify global 'a'
def h():
	global a
	a = 3
	print('Inside h() : ', a)


# Global scope
print('global : ', a)
f()
print('global : ', a)
g()
print('global : ', a)
h()
print('global : ', a)

