string = "text"

# center prints a copy of the string and padding included
new_string = string.center(6)
# output => " text "
# length => 6

# you can use any symbol as a fill character
new_string2 = string.center(10, "-")
# output => " text"
# length => 10

print(new_string)
print(new_string2)
