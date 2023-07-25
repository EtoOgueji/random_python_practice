from array import *

vals = array('i', [1, 2, -3, 4, 5])
# vals.reverse()

print(vals.buffer_info())
print(vals.typecode)

# for i in range(5):
#     print(vals[i])
#
# for e in vals:
#     print(e)
#
# print(vals)

# to make a copy of an array
newArr = array(vals.typecode, (a for a in vals))

newArr1 = array(vals.typecode, (a*a for a in vals))

i = 0

while i < len(newArr):
    print(newArr[i])
    i += 1
