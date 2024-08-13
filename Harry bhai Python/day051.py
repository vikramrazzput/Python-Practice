# List Methods

# reverse()
# This method reverses the order of the list.

# Example:

colors = ["voilet", "indigo", "blue", "green"]
colors.reverse()
print(colors)

num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.reverse()
print(num)

# Output:
# ['green', 'blue', 'indigo', 'voilet']
# [7, 9, 8, 2, 1, 2, 1, 6, 3, 5, 2, 4]

# ---------------------------------------------------------------------------------------------------------

# index()
# This method returns the index of the first occurrence of the list item.

# Example:

colors = ["voilet", "green", "indigo", "blue", "green"]
print(colors.index("green"))

num = [4,2,5,3,6,1,2,1,3,2,8,9,7]
print(num.index(3))

# Output:
# 1
# 3