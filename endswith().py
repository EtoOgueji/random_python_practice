#         0123456789
string = "Carol Shaw"


print(string.endswith("Shaw"))  # True
print(string.endswith("Carol Shaw"))  # True

# specifying a start index
print(string.endswith("Shaw", 4))  # "l Shaw" => True
print(string.endswith("Shaw", 7))  # "haw" => False
print(string.endswith("Shaw", 6, 10))  # "Shaw" => True
print(string.endswith("Sh", 6, 8))  # "Sh" => True
print(string.endswith("h", 6, 8))  # "Sh" => True

# using tuples
print(string.endswith(("Shaw", "Smith"))) # True
print(string.endswith(("Pratt", "Smith"))) # False




