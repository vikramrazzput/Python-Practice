"""

range(start, stop, step)

This syntax generates a sequence of numbers that starts counting at start (inclusive) and increments 
according to step until it reaches stop (non-inclusive).

"""

for num in range(10,21,2):
  print(num)

# output

# 10
# 12
# 14
# 16
# 18
# 20

for num in range(20, 11, -2):
  print(num)

# output

# 20
# 18
# 16
# 14
# 12


# Something to note is that step can be either a negative or positive number, but it cannot be 0.

# Something to note here is that you cannot pass float values to range().
