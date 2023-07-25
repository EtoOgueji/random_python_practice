# squares = []
# for x in range(10):
#     squares.append(x**2)
#


squares = list(map(lambda x: x**2, range(10)))
# or
# squares = [x**2 for x in range(10)]
print(squares)

comprehension = [(x, y) for x in [1, 2, 3] for y in [4, 5, 6] if x != y]
print(comprehension)

combs = []

for x in [1, 2, 3]:
    for y in [4, 5, 6]:
        if x != y:
            combs.append((x, y))
print(combs)