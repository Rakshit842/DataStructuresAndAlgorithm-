# Sum of two matrices

rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))

matrix1 = []
matrix2 = []
result = []

for i in range(rows):
    row = []
    for j in range(columns):
        value = int(input(f"Enter element at position [{i}][{j}]: "))
        row.append(value)
    matrix1.append(row)

for i in range(rows):
    row = []
    for j in range(columns):
        value = int(input(f"Enter element at position [{i}][{j}]: "))
        row.append(value)
    matrix2.append(row)

for i in range(rows):
    row = []
    for j in range(columns):
        row.append(matrix1[i][j] + matrix2[i][j])
    result.append(row)

for row in result:
    print(row)