# List Methods

# list.sort()
# This method sorts the list in ascending order. The original list is updated

# Example 1:

colors = ["voilet", "indigo", "blue", "green"]
colors.sort()
print(colors)

num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.sort()
print(num)

# Output:
# ['blue', 'green', 'indigo', 'voilet']
# [1, 1, 2, 2, 2, 3, 4, 5, 6, 7, 8, 9]


# What if you want to print the list in descending order?
# We must give reverse=True as a parameter in the sort method.

# Example:

colors = ["voilet", "indigo", "blue", "green"]
colors.sort(reverse=True)
print(colors)

num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.sort(reverse=True)
print(num)

# Output:
# ['voilet', 'indigo', 'green', 'blue']
# [9, 8, 7, 6, 5, 4, 3, 2, 2, 2, 1, 1]

# The reverse parameter is set to False by default.

# Note: Do not mistake the reverse parameter with the reverse method.
