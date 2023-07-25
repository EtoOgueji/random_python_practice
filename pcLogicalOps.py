user = "bob"
password = "abc"

if user == "bob" and password == "abc":
    print("Logged In!")
print()
# and
print("AND OPERATOR")
print("True and True: ", True and True)
print("True and False: ", True and False)
print("False and True: ", False and True)
print("False and False: ", False and False)

print()

# or
print("OR OPERATOR")
print("True or True: ", True or True)
print("True or False: ", True or False)
print("False or True: ", False or True)
print("False or False: ", False or False)

print()

# not
print("NOT OPERATOR")
print("not True: ", not True)
print("not False: ", not False)

print()

# beware of operator precedence!!
print(True or (4/0 == 0)) # = True but if they switch positions it will lead to ZDError

print(not False or True)