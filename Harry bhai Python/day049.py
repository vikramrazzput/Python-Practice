"""

List Comprehension
List comprehensions are used for creating new lists from other iterables like lists, tuples, dictionaries, sets, and even in arrays and strings.

Syntax:
List = [Expression(item) for item in iterable if Condition]

Expression: It is the item which is being iterated.

Iterable: It can be list, tuples, dictionaries, sets, and even in arrays and strings.

Condition: Condition checks if the item should be added to the new list or not.

"""

lst = [i for i in range(4)]
print(lst)  # [0, 1, 2, 3]

lst2 = [i*i for i in range (4)]
print (lst2)  # [0, 1, 4, 9]

lst3 = [i*i for i in range (10)]
print (lst3)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

lst4 = [i*i for i in range (10) if i%2==0]  # we can also add condition
print (lst4)  # [0, 4, 16, 36, 64]

# Example 1: Accepts items with the small letter “o” in the new list
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)

# Output:
# ['Milo', 'Bruno', 'Rosa']



# Example 2: Accepts items which have more than 4 letters
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if (len(item) > 4)]
print(namesWith_O)

# Output:
# ['Sarah', 'Bruno', 'Anastasia']