# While loop

i=0;
while (i<=3):
    print (i)
    i=i+1
print ("Done with the loop")

print ("new example")
count = 5
while (count > 0):
  print(count)
  count = count - 1

"""

Else with While Loop
We can even use the else statement with the while loop. Essentially what the else statement does is that 
as soon as the while loop condition becomes False, the interpreter comes out of the while loop and the else 
statement is executed.

"""
x = 5
while (x > 0):
    print(x)
    x = x - 1
else:
    print('counter is 0')

"""
OUTPUT:
5
4
3
2
1
counter is 0

"""    
# while loop ko jyada number ke saath nhi, complex situation main istemaal karte hain

# NOTE: python main Do-While loop nho hota