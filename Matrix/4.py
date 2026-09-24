# Rotaion of matrix in clockwise direction
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input(f"Enter element [{i}][{j}]: ")))
    matrix.append(row)

transpose = []
for i in range(cols):
    temp = []
    for j in range(rows):
        temp.append(matrix[j][i])
    transpose.append(temp)

for i in range(len(transpose)):
    transpose[i].reverse()

for row in transpose:
    print(*row)


#Rotation of matrix anit-clockwise
matrix = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]

rows = len(matrix)
cols = len(matrix[0])

transpose = []
for r in range(cols):
    row = []
    for c in range(rows):
        row.append(matrix[c][r])
    transpose.append(row)

for c in range(len(transpose[0])):
    top = 0
    bottom = len(transpose) - 1
    while top < bottom:
        transpose[top][c], transpose[bottom][c] = transpose[bottom][c], transpose[top][c]
        top += 1
        bottom -= 1

for row in transpose:
    print(row)
