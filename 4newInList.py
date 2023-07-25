def new_in_list(my_list, idx, element):

    if idx < 0:
        return new_in_list
    elif idx >= len(my_list):
        return new_in_list()
    else:
        list_copy = my_list.copy()
        list_copy[idx] = element
        return list_copy


my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = new_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)