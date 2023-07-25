# Random Access Memory: RAM
# Ask for a string

stringForAcr = input("Enter a string: ")

# convert string to uppercase
stringForAcr = stringForAcr.upper()

# convert the string into a list
stringForAcrList = stringForAcr.split()

# cycle through the list
for word in stringForAcrList:

    # get 1st letter of the word and eliminate the newline
    print(word[0], end="")

# add a newline
print()