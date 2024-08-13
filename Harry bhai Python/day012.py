"""

What are strings?
In python, anything that you enclose between single or double quotation marks is considered a string. 
A string is essentially a sequence or array of textual data. Strings are used when working with Unicode characters.

"""



name = "Harry";
friend = "Rohan";
anotherFriend = 'Lovish';

name = "Vikram";
print("Hello, " + name); # Hello, Vikram

# Sometimes, the user might need to put quotation marks in between the strings

print("He said, \"I want to eat an apple\".");
print('He said, "I want to eat an apple".');

# both are correct

# --------------------------------------------------------------------------------------------------------

# Multiline Strings

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# for multiline string, we have to put the string under ["""   """] (triple quote)