# String Slicing & Operations on String

# Length of a String
# We can find the length of a string using len() function.

fruit = "Mango"
len1 = len(fruit)
print("Mango is a", len1, "letter word.")

# function ke liye humlog parenthesis ka istemaal karte hain aur slicing ke liye square bracket ka istemaal karte hain

# ------------------------------------------------------------------------------------------------------

# slicing of a string

print(fruit[0:4]) # including 0 but not 4   # [starting_index : length]
print(fruit[1:4]) # including 1 but not 4   # [starting_index : length]
print(fruit[:5]) # agar starting_index nhi diya hua hai to usko 0 consider karenge

print(fruit[ : ]) # agar starting_index aur length nhi diya hua hai to starting_index = 0 & length = sizeof string mann lenge


print(fruit[0:-3]) # negative ke case main pytyhon automatic length of fruit before -ve length lga leta hain i.e. (5-3 = 2)
print(fruit[:len(fruit)-3]) # similar to above example

print (fruit[-1:len(fruit)-3]) 
# negative ke case main pytyhon automatic length of fruit before -ve length lga leta hain i.e. (5-1 = 4)
# print (fruit[4:2])  # ye possible nhi hain isliye nhi print ho rha kuch

print (fruit[-3:-1])  
 # negative ke case main pytyhon automatic length of fruit before -ve length lga leta hain i.e. (5-3 = 2 : 5-1 = 4)
#  print (fruit[4:2])  # iska value print hoga