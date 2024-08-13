# List Methods

# count()
# Returns the count of the number of items with the given value.

# Example:

colors = ["voilet", "green", "indigo", "blue", "green"]
print(colors.count("green"))

num = [4,2,5,3,6,1,2,1,3,2,8,9,7]

# Output:
# 2
# 3

# ---------------------------------------------------------------------------------------------------------

# insert():
# This method inserts an item at the given index. User has to specify index and the item to be inserted within the insert() method.

# Example:

colors = ["voilet", "indigo", "blue"]
#           [0]        [1]      [2]

colors.insert(1, "green")   #inserts item at index 1
# updated list: colors = ["voilet", "green", "indigo", "blue"]
#       indexs              [0]       [1]       [2]      [3]

print(colors)

# Output:
# ['voilet', 'green', 'indigo', 'blue']