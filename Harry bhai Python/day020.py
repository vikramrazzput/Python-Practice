"""

isspace() :
The isspace() method returns True only and only if the string contains white spaces, else returns False.

"""

str1 = "        "       #using Spacebar
print(str1.isspace())                        # True

str2 = "        "       #using Tab
print(str2.isspace())                        # True

str3 = "   a   "
print (str3.isspace())    # False

# -------------------------------------------------------------------------------------------------------------

"""

istitle() :
The istitile() returns True only if the first letter of each word of the string is capitalized, else it returns False.

"""

str1 = "World Health Organization" 
print(str1.istitle())  # True

str2 = "To kill a Mocking bird"
print(str2.istitle())   # False

# --------------------------------------------------------------------------------------------------------------

"""

isupper() :
The isupper() method returns True if all the characters in the string are upper case, else it returns False.

"""

str1 = "WORLD HEALTH ORGANIZATION" 
print(str1.isupper())   # True