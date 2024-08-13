# List in python

"""

Python Lists
• Lists are ordered collection of data items.
• They store multiple items in a single variable.
• List items are separated by commas and enclosed within square brackets [].
• Lists are changeable meaning we can alter them after creation.

"""


marks = [3,4,5,6]
print (marks)
print (type (marks)) # <class 'list'>

# python list ka bhi index 0 se start hota hain
print (marks[0]) # 3
print (marks[1]) # 4
print (marks[2]) # 5
print (marks[3]) # 6

# Example 1:

lst1 = [1,2,2,3,5,4,6]
lst2 = ["Red", "Green", "Blue"]
print(lst1) # [1, 2, 2, 3, 5, 4, 6]
print(lst2) # ['Red', 'Green', 'Blue']


# Example 2:

details = ["Abhijeet", 18, "FYBScIT", 9.8] 
print(details) # ['Abhijeet', 18, 'FYBScIT', 9.8]

# NOTE: As we can see, a single list can contain items of different data types.

