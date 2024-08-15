"""

 Range of Index:
You can print a range of tuple items by specifying where do you want to start, where do you want to end 
and if you want to skip elements in between the range.

Syntax:
Tuple[start : end : jumpIndex]

Note: jump Index is optional. We will see this in given examples.

"""


# Example: printing every 3rd consecutive withing given range

animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[1:8:3])

# Output:
# ('dog', 'pig', 'goat')

# NOTE: Here, jump index is 3. Hence it prints every 3rd element within given index.

"""

NOTE:
• Tuples are immutable
• Strings are immutable
• List are immutable

"""