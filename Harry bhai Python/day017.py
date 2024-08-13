# The replace() method replaces all occurences of a string with another string.

str2 = "Silver Spoon"
print(str2.replace("Sp", "M")) # Silver Moon


# The split() method splits the given string at the specified instance and returns the separated strings as list items.

str2 = "Silver Spoon"
print(str2.split(" "))      #Splits the string at the whitespace " ".

"""
OUTPUT
['Silver', 'Spoon']
There are various other string methods that we can use to modify our strings.
"""

"""
capitalize() :
The capitalize() method turns only the first character of the string to uppercase and the rest other 
characters of the string are turned to lowercase. The string has no effect if the first character is already 
uppercase.

"""

str1 = "hello"
capStr1 = str1.capitalize()
print(capStr1) # Hello
str2 = "hello WorlD"
capStr2 = str2.capitalize()
print(capStr2) # Hello world [world is not the first character of the string]

# --------------------------------------------------------------------------------------------------------

# center()
# The center() method aligns the string to the center as per the parameters given by the user.

str1 = "Welcome to the Console!!!"
print (len (str1))

print(str1.center(50))
print ( len (str1.center(50)))

"""
OUTPUT:
25
            Welcome to the Console!!!                  #[gap in the begining and end is due to center()]
50
"""

# We can also provide padding character. It will fill the rest of the fill characters provided by the user.

str1 = "Welcome to the Console!!!"
print (len (str1))

print(str1.center(50, "."))
print ( len (str1.center(50, ".")))

"""
OUTPUT:
25
............Welcome to the Console!!!.............  # [12 dot is before and 13 dot is after .Welcome to the Console!!! ]
50
"""
