import random
import math

#generate a 10 * 10 list of lists
# multiDList = [[0] * 10 for i in range(10)]
#
# multiDList[0][1] = 10
#
# print(multiDList[1][1])

listTable = [[0] * 4 for i in range(4)]

for i in range(4):
    for j in range(4):
        listTable[i][j] = "{} : {}".format(i, j)

for i in range(4):
    for j in range(4):
        print(listTable[i][j], end=" || ")
    print()