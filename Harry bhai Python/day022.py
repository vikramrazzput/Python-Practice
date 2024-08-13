#  if-else

a = int(input("Enter your age: "))
print("Your age is:", a)

# Conditional operators 
# >, <, >=, <=, ==, !=
print(a>18)
print(a<=18)
print(a==18)
print(a!=18)

# =========================================================================================================

# indentation is important in python for if-else statement

if(a>18):
  print("You can drive")
  print("Yes")
else:
  print("You cannot drive")
  print("No")
print("Yay!")  # NOTE: here print("Yay!") is not the part of else statement


applePrice = 10
budget = 200
if (budget - applePrice > 50):
    print("Alexa, add 1 kg Apples to the cart.")
else:
    print("Alexa, do not add Apples to the cart.")
