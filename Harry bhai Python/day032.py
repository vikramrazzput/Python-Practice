# NOTE: python main Do-While loop nho hota

"""

How to emulate do while loop in python?
To create a do while loop in Python, you need to modify the while loop a bit in order to get similar
 behavior to a do while loop.

The most common technique to emulate a do-while loop in Python is to use an infinite while loop with a break 
statement wrapped in an if statement that checks a given condition and breaks the iteration if that condition 
becomes true:

"""

while True:
  number = int(input("Enter a positive number: "))
  print(number)
  if not number > 0:
    break
  
"""
OUTPUT:
Enter a positive number: 1
1
Enter a positive number: 4
4
Enter a positive number: -1
-1
"""

"""
EXPLANATION:
This loop uses True as its formal condition. This trick turns the loop into an infinite loop. Before the 
conditional statement, the loop runs all the required processing and updates the breaking condition. If this 
condition evaluates to true, then the break statement breaks out of the loop, and the program execution continues 
its normal path.
"""