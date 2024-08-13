"""

Range of Index:
You can print a range of list items by specifying where you want to start, where do you want to end and 
if you want to skip elements in between the range.

Syntax:

listName[start : end : jumpIndex]

Note: jump Index is optional. We will see this in later examples.

"""

# Example: Printing alternate values

animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[::2])		#using positive indexes
print(animals[-8:-1:2])	#using negative indexes

# Output:
# ['cat', 'bat', 'pig', 'donkey', 'cow']
# ['dog', 'mouse', 'horse', 'goat']

# NOTE: Here, we have not provided start and index, which means all the values will be considered. 
# But as we have provided a jump index of 2 only alternate values will be printed.


# Example: printing every 3rd consecutive value withing a given range

animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[1:8:3])

# Output:
# ['dog', 'pig', 'goat

# NOTE: Here, jump index is 3. Hence it prints every 3rd element within given index.