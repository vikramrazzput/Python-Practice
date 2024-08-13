# List Methods

# append():
# This method appends items to the end of the existing list.

# Example:

colors = ["voilet", "indigo", "blue"]
colors.append("green")
print(colors)

# Output:
# ['voilet', 'indigo', 'blue', 'green']

# ------------------------------------------------------------------------------------------------------

# extend():
# This method adds an entire list or any other collection datatype (set, tuple, dictionary) to the existing list.

# Example 1:

# add a list to a list
colors = ["voilet", "indigo", "blue"]
rainbow = ["green", "yellow", "orange", "red"]
colors.extend(rainbow)
print(colors)  # here, colors value get updated
print (rainbow)

# Output:
# ['voilet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']
# ['green', 'yellow', 'orange', 'red']

