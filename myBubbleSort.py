import random
import math

# 1. An outer loop decreases in size each time
# 2. The goal is to have the largest number at the end of the list when the outer loop completes 1 cycle
# 3. The inner loop starts comparing indexes at the beginning of the looping
# 4. Check if list[Index] > list[Index + 1]
# 5. If so swap the index values
# 6. When the inner loop completes the largest number is at the end of the list
# 7. Decrement the outer loop by 1

noList = []

for i in range(5):
    noList.append(random.randrange(1, 11))


print(noList, "\n")

i = len(noList) - 1

while i > 1:

    j = 0
    while j < i:
        if noList[j] > noList[j+1]:

            print("swap required")

            temp = noList[i]
            noList[j] = noList[j+1]
            noList[j+1] = temp


        else:
            print("No swap needed")
        j += 1

        for k in noList:
            print(k, end=", ")
        print()
    i -= 1

