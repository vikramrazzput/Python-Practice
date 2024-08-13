# tuples in python

tup = (1,2,3)
print (type(tup), tup)  # <class 'tuple'> (1, 2, 3)

tup2 = (1,2)
print (type(tup2), tup2)  # <class 'tuple'> (1, 2)

tup3 = (1)
print (type(tup3), tup3) # <class 'int'> 1
# this above condition is very confusing for python because it treat above tuple as integer

# to avoid above condition  # tuple main hum comma (,) lagayenge
tup4 = (1,)
print (type(tup4), tup4)  # <class 'tuple'> (1,)
 