# Tuple Indexes

# Each item/element in a tuple has its own unique index. This index can be used to access any particular 
# item from the tuple. The first item has index [0], second item has index [1], third item has index [2] 
# and so on.

# Example:

country = ("Spain", "Italy", "India",)
#            [0]      [1]      [2]

"""

Accessing tuple items:
I. Positive Indexing:
As we have seen that tuple items have index, as such we can access items using these indexes.

"""

# Example:

country = ("Spain", "Italy", "India",)
#            [0]      [1]      [2]  
   
print(country[0])  # Spain
print(country[1])  # Italy
print(country[2])  # India

"""

II. Negative Indexing:
Similar to positive indexing, negative indexing is also used to access items, but from the end of the tuple. 
The last item has index [-1], second last item has index [-2], third last item has index [-3] and so on.

"""

# Example:

country = ("Spain", "Italy", "India", "England", "Germany")
#            [0]      [1]      [2]       [3]        [4]
print(country[-1]) # Similar to print(country[len(country) - 1])
print(country[-3])
print(country[-4])

# Output:
# Germany
# India
# Italy
