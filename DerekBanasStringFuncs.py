rand_string = "      this is an important string   "

# get rid of the white space at the left
rand_string = rand_string.lstrip()

# get rid of the white space at the right
rand_string = rand_string.rstrip()

# get rid of all white spaces both left and right
rand_string = rand_string.strip()

# capitalize first character
print(rand_string.capitalize())

# transform all characters to uppercase
print(rand_string.upper())

# transform all to lowercase
print(rand_string.lower())

a_list = ["Bunch", "of", "random", "words"]
print(" ".join(a_list))

a_list_2 = rand_string.split()
for i in a_list_2:
    print(i)
print("How many is: ", rand_string.count("is"))

print("Where is string: ", rand_string.find("string"))

print(rand_string.replace("an ", "a kind of "))