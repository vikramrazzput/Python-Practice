# Shows time of your desktop

import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)
# https://docs.python.org/3/library/time.html#time.strftime

# ------------------------------------------------------------------------------------------------------------

"""
Create a python program capable of greeting you with Good Morning, Good Afternoon and Good Evening. 
Your program should use time module to get the current hour.
"""

# first we need to convert the string into integer
timestamp = int(time.strftime('%H'));

if (6 <= timestamp and timestamp < 12):
    print ("Good Morning")
elif (12 <= timestamp and timestamp < 18):
    print ("Good Afternoon")
elif (18 <= timestamp and timestamp < 21):
    print ("Good Evening")
else :
    print ("Good Night")

# this is done by harry
import time
t = time.strftime('%H:%M:%S') 
hour = int(time.strftime('%H'))
# hour = int(input("Enter hour: "))
# print(hour)

if(hour>=0 and hour<12):
  print("Good Morning Sir!")
elif(hour>=12 and hour<17):
  print("Good Afternoon Sir!")
elif(hour>=17 and hour<0):
  print("Good Night Sir!")