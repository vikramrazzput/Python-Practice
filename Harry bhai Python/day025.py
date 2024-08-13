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