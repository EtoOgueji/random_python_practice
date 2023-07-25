"""
    #
   ###
  #####
 #######
#########
    #
"""


height = input("Enter height of a tree: ")

height = int(height)

spaces = height - 1

hashes = 1

stumpSpaces = height - 1


while (height != 0):
    for i in range(spaces):
        print(' ', end="")
    for j in range(hashes):
        print("#", end="")
    print()
    hashes += 2

    spaces -= 1

    height -= 1

for i in range(stumpSpaces):
    print(' ', end="")
print('#')
