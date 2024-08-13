# List Methods

l = [11, 45, 1, 2, 4, 6, 1, 1]
print(l)  # [11, 45, 1, 2, 4, 6, 1, 1]

m=l
m[0] = 0
print (l)  # [0, 45, 1, 2, 4, 6, 1, 1]
# from this we conclude that, pass by reference taken place here
# i.e. list follows the principle of pass by reference

# so to resolve this problem, we use 

# copy()
# Returns copy of the list. This can be done to perform operations on the list without modifying the original list.

# Example:

colors = ["voilet", "green", "indigo", "blue"]
newlist = colors.copy()
print(colors)
print(newlist)

# Output:
# ['voilet', 'green', 'indigo', 'blue']
# ['voilet', 'green', 'indigo', 'blue']