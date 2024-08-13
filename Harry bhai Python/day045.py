"""

Check whether an item in present in the list?
We can check if a given item is present in the list. This is done using the in keyword.

"""


colors = ["Red", "Green", "Blue", "Yellow", "Green"]
if "Yellow" in colors:
    print("Yellow is present.")
else:
    print("Yellow is absent.")

# Yellow is present.



colors = ["Red", "Green", "Blue", "Yellow", "Green"]
if "Orange" in colors:
    print("Orange is present.")
else:
    print("Orange is absent.")

# Orange is absent.

# VVIP: Same thing applies for strings as well!

if "Ha" in "Harry":
  print("Yes")
else:
    print ("No")

if "rry" in "Harry":
  print("Yes")
else:
    print ("No")

if "Hay" in "Harry":
  print("Yes")  
else:
    print ("No")
