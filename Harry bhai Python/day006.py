"""
Data type specifies the type of value a variable holds. This is required in programming to do various 
operations without causing an error.
In python, we can print the type of any operator using type function:

"""

''' 
    1. Numeric data: int, float, complex
    int: 3, -8, 0
    float: 7.349, -9.0, 0.0000001
    complex: 6 + 2i

'''
# for int
a = 5;
print (a); # 5
print("The type of a is ", type(a)); # <class 'int'>

# for float
a1 = 5.5;
print (a1); # 5.5
print("The type of a1 is ", type(a1)); # <class 'float'>

# for complex (python main complex no bhi bna sakte hain)
a2 = complex(5,2);
print (a2); # (5+2j)
print("The type of a2 is ", type(a2)); # <class 'complex'>
