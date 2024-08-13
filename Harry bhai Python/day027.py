# FOR LOOP in python

"""

The for Loop
for loops can iterate over a sequence of iterable objects in python. 
Iterating over a sequence is nothing but iterating over strings, lists, tuples, sets and dictionaries.

"""

# Example: iterating over a string:

name = 'Abhishek'
for i in name:
  print(i)

name = 'Abhishek'
for i in name:
    print(i, end=", ")  # A, b, h, i, s, h, e, k,

# Example: iterating over a list:

colors = ["Red", "Green", "Blue", "Yellow"]
for x in colors:
    print(x)
    for i in x:
       print (i)

