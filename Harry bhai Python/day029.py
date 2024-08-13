"""

range(start, stop)

This syntax generates a sequence of numbers based on the start (inclusive) and stop (non-inclusive) values 
that increment by 1.

"""

for k in range(1, 5):
  print(k)
# ye wala loop [ 1 se lekar 4 tak value print karega]  # means k 1 se start hoga yahan

for k in range(1, 5):
  print(k+1)
# ye wala loop [ 2 se lekar 5 tak value print karega]  # means k 2 se start hoga yahan

# You can pass negative integer values to range() as well:

for num in range(-5, 1):
  print(num)

# output

# -5
# -4
# -3
# -2
# -1
# 0

# Something to note here is that you cannot pass float values to range().s