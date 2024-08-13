"""

Range of Index:
You can print a range of list items by specifying where you want to start, where do you want to end and 
if you want to skip elements in between the range.

Syntax:

listName[start : end : jumpIndex]

Note: jump Index is optional. We will see this in later examples.

"""

# Example: printing all element from a given index till the end

animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[4:])	#using positive indexes
print(animals[-4:])	#using negative indexes  # [len(animals) - 4]

# Output:
# ['pig', 'horse', 'donkey', 'goat', 'cow']
# ['horse', 'donkey', 'goat', 'cow']

# NOTE: When no end index is provided, the interpreter prints all the values till the end.


# Example: printing all elements from start to a given index

animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[:6])	#using positive indexes
print(animals[:-3])	#using negative indexes

# Output:
# ['cat', 'dog', 'bat', 'mouse', 'pig', 'horse']
# ['cat', 'dog', 'bat', 'mouse', 'pig', 'horse']

# NOTE: When no start index is provided, the interpreter prints all the values from start up to the end index provided.

# Example: printing all elements from start to the end 

animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[:])	#using positive indexes
print(animals[0:9])	#using negative indexes
print(animals[0:len(animals)])	
print(animals[0:])	

# OUTPUT:
# ['cat', 'dog', 'bat', 'mouse', 'pig', 'horse', 'donkey', 'goat', 'cow']
# ['cat', 'dog', 'bat', 'mouse', 'pig', 'horse', 'donkey', 'goat', 'cow']
# ['cat', 'dog', 'bat', 'mouse', 'pig', 'horse', 'donkey', 'goat', 'cow']
# ['cat', 'dog', 'bat', 'mouse', 'pig', 'horse', 'donkey', 'goat', 'cow']