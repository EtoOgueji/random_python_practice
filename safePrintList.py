# returns the no of elements of a list and returns the list itself

def safe_print_list(my_list=[], x=0):
    total = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            total += 1
        except IndexError:
            break
        print("")
        return total
