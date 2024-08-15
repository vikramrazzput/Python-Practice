# Manipulating Tuples

# we convert the tuple to a list, manipulate items of the list using list methods, then convert list back to a tuple.

# However, we can directly concatenate two tuples without converting them to list.

# Example:

countries = ("Pakistan", "Afghanistan", "Bangladesh", "SriLanka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = countries + countries2
print(southEastAsia)

# Output:
# ('Pakistan', 'Afghanistan', 'Bangladesh', 'SriLanka', 'Vietnam', 'India', 'China')