# Taking User Input in python

""" In python, we can take user input directly by using input() function.This input function gives a 
  return value as string/character hence we have to pass that into a variable   """

# VVIP: input function returns the value as string. Hence we have to typecast them whenever required to another datatype.

a = input(); # vikram
print ("My name is", a); # My name is vikram

# input ke ander humlog string bhi dal sakte hain
a = input("Enter your name: "); # Enter your name: harry
print ("My name is", a); # My name is harry


# -----------------------------------------------------------------------------------------------------------

x = input("Enter first number: ") # 100
y = input("Enter second number: ") # 12
print(x  + y) # problem occur # concatenation of string happened # 10012
# input function returns the value as string. Hence we have to typecast them whenever required to another datatype.

print(int(x) + int(y)); # 112
