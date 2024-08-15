# tuples in python

"""

Python Tuples
Tuples are ordered collection of data items. They store multiple items in a single variable. Tuple items are 
separated by commas and enclosed within round brackets (). Tuples are unchangeable meaning we can not alter 
them after creation.

"""


tup = (1,2,3)
print (type(tup), tup)  # <class 'tuple'> (1, 2, 3)

tup2 = (1,2)
print (type(tup2), tup2)  # <class 'tuple'> (1, 2)

tup3 = (1)
print (type(tup3), tup3) # <class 'int'> 1
# this above condition is very confusing for python because it treat above tuple as integer

# to avoid above condition  # tuple main hum comma (,) lagayenge
tup4 = (1,)
print (type(tup4), tup4)  # <class 'tuple'> (1,)

# Example 1:

tuple1 = (1,2,2,3,5,4,6)
tuple2 = ("Red", "Green", "Blue")
print(tuple1)
print(tuple2)

# Output:
# (1, 2, 2, 3, 5, 4, 6)
# ('Red', 'Green', 'Blue')
# Example 2:

details = ("Abhijeet", 18, "FYBScIT", 9.8)
print(details)

# Output:
# ('Abhijeet', 18, 'FYBScIT', 9.8)

# NOTE: in tuple we can store data any data type
 