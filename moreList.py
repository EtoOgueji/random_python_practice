import random
import math

numList = []

for i in range(5):
    numList.append(random.randrange(1, 10))

numList.sort()

numList.reverse()

numList.index(5, 10)

numList.remove(10)

numList.pop(2)



for k in numList:
    print(k, end=", ")
print()