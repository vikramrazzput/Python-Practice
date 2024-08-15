# Tuple methods

# As tuple is immutable type of collection of elements it have limited built in methods.

"""

count() Method
The count() method of Tuple returns the number of times the given element appears in the tuple.

Syntax:
tuple.count(element)

"""

# Example
Tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = Tuple1.count(3)
print('Count of 3 in Tuple1 is:', res)  # 3

# ===============================================================================================================

"""

index() method
The Index() method returns the first occurrence of the given element from the tuple.

Syntax:
tuple.index(element, start, end)
Note: This method raises a ValueError if the element is not found in the tuple.

"""

# Example

Tuple = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = Tuple.index(3) 
print('First occurrence of 3 is', res)  # 3

# if we want to find the occurrence of the given element in the tuple between the index 4 to 6

res = Tuple.index(3,4,6) # (element, start, end)
print (res) # this will return the index of tuple

# length of tuple is'
print (len(Tuple))