# Strings are immutable (we cannot change them) 
# NOTE: we cannot change strings inplace

# The upper() method converts a string to upper case.

a = "Harry";
print (a.upper()); # a new string is created where upper case string is stored
# existing string ko change nhi karega, new string bna dega

# The lower() method converts a string to lower case.
print (a.lower()); # a new string is created where upper case string is stored
# existing string ko change nhi karega, new string bna dega

# _________________________________________________________________________________________________________

# The strip() method removes any white spaces before and after the string.

str2 = " Silver Spoon ";
print(str2.strip()); #Silver Spoon

# the rstrip() removes any trailing characters.

str3 = "Hello !!!"
print(str3.rstrip("!")) # Hello

# NOTE: rstrip() only removes trailing characters. It will not remove begining characters
str4 = "!!!Hello!!!"
print (str4.rstrip("!")) # !!!Hello