# Range of Index:

"""

 Range of Index:
You can print a range of tuple items by specifying where do you want to start, where do you want to end 
and if you want to skip elements in between the range.

Syntax:
Tuple[start : end : jumpIndex]

Note: jump Index is optional. We will see this in given examples.

"""

# Example: printing all elements from start to a given index

animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[:6])      #using positive indexes
print(animals[:-3])     #using negative indexes

# Output:
# ('cat', 'dog', 'bat', 'mouse', 'pig', 'horse')
# ('cat', 'dog', 'bat', 'mouse', 'pig', 'horse')

# NOTE: When no start index is provided, the interpreter prints all the values from start up to the end index provided.

# ==========================================================================================================

# Example: Print alternate values

animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[::2])     #using positive indexes
print(animals[-8:-1:2]) #using negative indexes

# Output:
# ('cat', 'bat', 'pig', 'donkey', 'cow')
# ('dog', 'mouse', 'horse', 'goat')

# NOTE: Here, we have not provided start and end index, which means all the values will be considered. But as we 
# have provided a jump index of 2 only alternate values will be printed.