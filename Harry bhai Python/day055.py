# List Methods

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

# =============================================================================================================

# Concatenating two lists:
# You can simply concatenate two lists to join two lists.

# Example:

colors = ["voilet", "indigo", "blue", "green"]
colors2 = ["yellow", "orange", "red"]

k = colors + colors2
print (k)
print(colors + colors2)

# Output:
# ['voilet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']

# NOTE:the main difference between extend () and Concatenating two lists is that in extend() we update the original
# list but that is not the case for Concatenating two lists