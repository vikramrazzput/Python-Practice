# Range of Index:

"""

 Range of Index:
You can print a range of tuple items by specifying where do you want to start, where do you want to end 
and if you want to skip elements in between the range.

Syntax:
Tuple[start : end : jumpIndex]

Note: jump Index is optional. We will see this in given examples.

"""

# Example: Printing elements within a particular range:

animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[3:7])     #using positive indexes
print(animals[-7:-2])   #using negative indexes

# Output:
# ('mouse', 'pig', 'horse', 'donkey')
# ('bat', 'mouse', 'pig', 'horse', 'donkey')

# NOTE: Here, we provide index of the element from where we want to start and the index of the element till which we want to print the values. 
# Note: The element of the end index provided will not be included.

# ===========================================================================================================

# Example: Printing all element from a given index till the end

animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[4:])      #using positive indexes
print(animals[-4:])     #using negative indexes

# Output:
# ('pig', 'horse', 'donkey', 'goat', 'cow')
# ('horse', 'donkey', 'goat', 'cow')

# NOTE: When no end index is provided, the interpreter prints all the values till the end.