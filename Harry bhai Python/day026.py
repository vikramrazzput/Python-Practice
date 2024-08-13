# Match case statement (# Most recent feature of python started from python 3.10)

# similar to Switch Case statement in c++

"""

A match statement will compare a given variable’s value to different shapes, also referred to as the pattern. 
The main idea is to keep on comparing the variable with all the present patterns until it fits into one.

CODE:
match variable_name:
            case ‘pattern1’ : //statement1
            case ‘pattern2’ : //statement2
            …            
            case ‘pattern n’ : //statement n

"""



x = int(input("Enter the value of x: "))
# x is the variable to match
match x:
    # if x is 0
    case 0:
        print("x is zero")
    # case with if-condition
    case 4:
        print("case is 4")

    case _ if x!=90:
        print(x, "is not 90")
    case _ if x!=80:
        print(x, "is not 80")
    case _:
        print(x)
# default case ke syntax main underscore ( _ ) part hain
# unlike c++ we don't need to mention break statement after each statement

# Example 2

x = 4
# x is the variable to match
match x:
    # if x is 0
    case 0:
        print("x is zero")
    # case with if-condition
    case 4 if x % 2 == 0:
        print("x % 2 == 0 and case is 4")
    # Empty case with if-condition
    case _ if x < 10:
        print("x is < 10")
    # default case(will only be matched if the above cases were not matched)
    # so it is basically just an else:
    case _:
        print(x)

"""

OUTPUT:
x % 2 == 0 and case is 4

"""