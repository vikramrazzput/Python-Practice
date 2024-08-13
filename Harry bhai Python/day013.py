# Accessing Characters of a String

# In Python, string is like an array of characters. We can access parts of string by using its index which starts from 0.
# Square brackets can be used to access elements of the string.

name = "Harry";
#  indexing
# print(name) 
print(name[0]);
print(name[1]);
print(name[2]);
print(name[3]);
print(name[4]);
# print(name[5]) # Throws an error

# Looping through the string
print("Lets use a for loop\n")
for character in name:
    print(character);   


abcd = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

print("Lets use a for loop\n")
for character in abcd:
    print(character);  