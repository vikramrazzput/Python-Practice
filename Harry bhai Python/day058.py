# tuple in python

# Check for item:
# We can check if a given item is present in the tuple. This is done using the in keyword.

# Example 1:

country = ("Spain", "Italy", "India", "England", "Germany")
if "Germany" in country:
    print("Germany is present.")
else:
    print("Germany is absent.")

# Output:
# Germany is present.


# Example 2:

country = ("Spain", "Italy", "India", "England", "Germany")
if "Russia" in country:
    print("Russia is present.")
else:
    print("Russia is absent.")

# Output:
# Russia is absent.