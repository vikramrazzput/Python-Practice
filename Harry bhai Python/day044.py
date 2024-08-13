# Indexing in list

"""

List Index
Each item/element in a list has its own unique index. This index can be used to access any particular item 
from the list. The first item has index [0], second item has index [1], third item has index [2] and so on.

Example:
colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [0]      [1]     [2]      [3]      [4]


Accessing list items
We can access list items by using its index with the square bracket syntax []. For example colors[0] will 
give "Red", colors[1] will give "Green" and so on...

"""

"""

Positive Indexing:
As we have seen that list items have index, as such we can access items using these indexes.
"""

# Example:
colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [0]      [1]     [2]      [3]      [4]

print(colors[2]) # Blue
print(colors[4]) # Green
print(colors[0]) # Red


"""

Negative Indexing:
Similar to positive indexing, negative indexing is also used to access items, but from the end of the list. 
The last item has index [-1], second last item has index [-2], third last item has index [-3] and so on.

"""

# Example:

colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [-5]    [-4]    [-3]     [-2]      [-1]

print(colors[-1]) # Green 
print(colors[-3]) # Blue
print(colors[-5]) # Red

# Important trick (very helpful trick)

print(colors[-3]) # Negative index
print(colors[len(colors)-3]) # Positive index
print(colors[5-3]) # Positive index
print(colors[2]) # Positive index

