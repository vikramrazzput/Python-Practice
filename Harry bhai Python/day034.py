# function in python

# a=9,b=8 # Incorrect Variable Assignment:
# In Python, you should assign variables using the = operator without commas. The line a=9,b=8 is incorrect. 
# You need to assign each variable separately or use tuple unpackin

a=9
b=8
gmean1 = (a*b)/(a+b)
print(gmean1)

# c=8,d=7 # Incorrect Variable Assignment:
# In Python, you should assign variables using the = operator without commas. The line a=9,b=8 is incorrect. 
# You need to assign each variable separately or use tuple unpackin

c=8
d=7
gmean2 = (c*d)/(c+d)
print(gmean2)

# to simplify this we use function

def calculateGmean (a,b):
    mean = (a*b)/(a+b)
    print (mean)

calculateGmean (9,8)
calculateGmean (8,7)