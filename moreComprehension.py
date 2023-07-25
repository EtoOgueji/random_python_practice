vec = [1, 2, 3, 4, 5]

[x * 2 for x in vec] # to create a new list with values doubled

[x for x in vec if x >= 0] # to exclude -ve numbers

[abs(x) for x in vec] # apply a function to all the elements

freshfruit = [' banana', ' loganberry ', 'passion fruit ']

[weapon.strip() for weapon in freshfruit] # call a method on each element

[(x, x**2) for x in range(6)] # create a list of 2-tuples like (num, sqr)

vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
[num for elem in vec for num in elem]