# Enter a string to hide in uppercase: HIDE

# secret message: 2320329923

# Original Message: HIDE

# Input "Enter a string to hide in uppercase"
norm_string = input("Enter a string to hide in uppercase: ")

secret_string = ""

# cycle through each character in the string
for char in norm_string:

    # store each character code in a new string
    secret_string += str(ord(char))

# Print "Secret Message: 8595859595"
print("Secret Message: ", secret_string)

# cycle through each character code 2 at a time by incrementing by 2 each time
norm_string = ""
for i in range(0, len(secret_string)-1, 2):

    # get the 1st and 2nd for the 2-digit number
    char_code = secret_string[i] + secret_string[i+1]

    # convert the code into characters and add them to a new string
    norm_string += chr(int(char_code))

print("Original Message: ", norm_string)
