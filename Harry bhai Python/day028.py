"""

range():
What if we do not want to iterate over a sequence? What if we want to use for loop for a specific number of times?


The range() function accepts three arguments - one is required, and two are optional.

"""
"""

By default, the syntax for the range() function looks similar to the following:

range(stop)

The stop argument is required.

The range() function returns a sequence of numbers starting from 0, incrementing by 1, and ending at 
the value you specify as stop (non-inclusive).

"""
for k in range(5):
  print(k)
# ye wala loop [ 0 se lekar 4 tak value print karega]  # means k 0 se start hoga yahan

# -------------------------------------------------------------------------------------------------------
for k in range(-5):
  print(k)

# agar range ka value negative hua to hum us loop ko ignore kar denge

# -------------------------------------------------------------------------------------------------------  



for k in range(0,5):
  print(k)
# ye wala loop [ 0 se lekar 4 tak value print karega]  # means k 0 se start hoga yahan


for k in range(5):
  print(k + 1)
# ye wala loop [ 1 se lekar 5 tak value print karega]  # means k 1 se start hoga yahan


# Something to note here is that you cannot pass float values to range().
