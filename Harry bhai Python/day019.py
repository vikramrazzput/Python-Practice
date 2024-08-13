"""

isalnum() :
The isalnum() method returns True only if the entire string only consists of A-Z, a-z, 0-9. 
If any other characters or punctuations are present, then it returns False.

"""

str1 = "Welcome001"
print(str1.isalnum())  # True

"""

isalpha() :
The isalnum() method returns True only if the entire string only consists of A-Z, a-z. 
If any other characters or punctuations or numbers(0-9) are present, then it returns False.

"""

str1 = "Welcome001"
print(str1.isalpha()) # False

# -----------------------------------------------------------------------------------------------------------

"""

islower() :
The islower() method returns True if all the characters in the string are lower case, else it returns False.

"""

str1 = "hello world"
print(str1.islower())  # True

# -----------------------------------------------------------------------------------------------------------

"""

isprintable() :
The isprintable() method returns True if all the values within the given string are printable, 
if not, then return False.

"""

str1 = "We wish you a Merry Christmas"
print(str1.isprintable())  # True

str2 = "We wish you a Merry Christmas \n"
print(str2.isprintable())  # False  (since \n is not printable )

