# count() :
# The count() method returns the number of times the given value has occurred within the given string.

str2 = "Abracadabra"
countStr = str2.count("a")
print(countStr)  # 4


# endswith() :
# The endswith() method checks if the string ends with a given value. If yes then return True, else return False.

str1 = "Welcome to the Console !!!"
print(str1.endswith("!!!")) # True

# We can even also check for a value in-between the string by providing start and length of index positions.

str1 = "Welcome to the Console !!!"
print(str1.endswith("to", 4, 10)) # True

# ------------------------------------------------------------------------------------------------------------

"""

find() :
The find() method searches for the first occurrence of the given value and returns the index where it is present. 
If given value is absent from the string then return -1.

"""

str1 = "He's name is Dan. He is an honest man."
print(str1.find("is")) # 10

"""

As we can see, this method is somewhat similar to the index() method. 
The major difference being that index() raises an exception if value is absent whereas find() does not.

"""

str1 = "He's name is Dan. He is an honest man."
print(str1.find("Daniel"))  # -1

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""

index() :
The index() method searches for the first occurrence of the given value and returns the index where it is present. 
If given value is absent from the string then raise an exception.

"""

str1 = "He's name is Dan. Dan is an honest man."
print(str1.index("Dan")) # 13

"""

As we can see, this method is somewhat similar to the find() method. 
The major difference being that index() raises an exception if value is absent whereas find() does not.

"""

str1 = "He's name is Dan. Dan is an honest man."
print(str1.index("Daniel"))

"""

OUTPUT:
ValueError: substring not found

"""


