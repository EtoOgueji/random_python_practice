import random
import math

# numList = []
# for i in range(5):
#     numList.appen(random.randrange(1, 10))
#
# numList.insert(5, 10)
#
# numList.remove(10)
#
# numList.pop(2)
#
# for k in numList:
#     print(k, end=", ")
# print()

# list comprehensions

evenList = [i * 2 for i in range(10)]

for i in evenList:
    print(i)

numList = [1, 2, 3, 4, 5]

listOfValues = [[math.pow(m, 2), math.pow(m, 3), math.pow(m, 4)]
                for m in numList]

for i in listOfValues:
    print(i)
print()

# generate a 10 by 10 list of list
multiDList = [[0] * 10 for i in range(10)]

multiDList[0][1] = 10

print(multiDList[0][1])