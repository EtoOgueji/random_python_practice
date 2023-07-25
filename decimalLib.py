from decimal import Decimal as D
#
# sum = D(0)
# sum += D("0.1")
# sum += D("0.1")
# sum += D("0.1")
# sum -= D("0.3")
#
# print("Sum =", sum)
#
# print(".1 + .1 + .1 - .3", .1 + .1 + .1 - .3)
# print("A =", ord("A"))
# print("65 =", chr(65))

name = input("Enter a string to hide in uppercase: ")


nameLen = len(name)
nameUni = []

for i in range(nameLen):
    nameUni.append(ord(name[i]))
print("Secret Message: ", end="")

for i in nameUni:
    print("{}".format(i), end="")
print()
print("Original Message: ", end="")
for i in name:
    print(i, end="")
