def no_c(my_string):
    for i in my_string:
        if my_string[i] == 'c' or my_string[i] == 'C':
            my_string.remove('cC')
    return my_string

print(no_c("Best School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))