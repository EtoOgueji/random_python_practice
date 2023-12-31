from math import pi
[str(round(pi, i)) for i in range(1, 6)]


matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

# [[row[i] for row in matrix] for i in range(4)] # transposes the matrix

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])


print(transposed)