
matrix = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
for i in range(len(matrix)):
    matrix[i][i] = 1

for i in range(len(matrix)):
    for j in range(len(matrix)):
        if i==j:
            print("1", end=" ")
        else:
            print("0", end=" ")
    print("")