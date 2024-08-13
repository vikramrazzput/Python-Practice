"""

Range of Index:
You can print a range of list items by specifying where you want to start, where do you want to end and 
if you want to skip elements in between the range.

Syntax:

listName[start : end : jumpIndex]

Note: jump Index is optional. We will see this in later examples.

"""

# Example: printing elements within a particular range:

animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[3:7])	    #using positive indexes
print(animals[-7:-2])	#using negative indexes    # [len(animals) - 7 : len(animsls) - 2]

# Output:
# ['mouse', 'pig', 'horse', 'donkey']
# ['bat', 'mouse', 'pig', 'horse', 'donkey']

"""

NOTE: Here, we provide index of the element from where we want to start and the index of the element till 
      which we want to print the values.

Note: The element of the end index provided will not be included.

"""