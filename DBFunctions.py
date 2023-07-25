glbName = "EtoTheGoat"

def add_numbers(num1, num2):
    return num1 + num2

def change_name(name):
    return "Mark"

name = "Eto"

name = change_name(name)

print(name)

def change_name2(name):
    global glbName
    glbName = "EtoTheGreat"

print(glbName)

def get_sum(num1, num2):
    sum = num1 + num2

print(get_sum(5, 6)) # None