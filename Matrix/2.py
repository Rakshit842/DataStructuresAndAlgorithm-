
Rows = int(input("Enter row: "))
Columns = int(input("EnterColumns: "))

matrix = []

for i in range(Rows):
    row = []
    for j in range(Columns):
        value = int(input("Enter value for position ((i), (j)): ")) 
        row.append(value)
    matrix.append(row)

print("Matrix: ")
for r in matrix: 
    print(r)

# Code for row wise traversal 
for rowIndex in range(Rows):
    for colIndex in range(Columns):
        print(matrix[rowIndex][colIndex], end = " ")
    print()

#code for column wise traversal
for colIndex in range(Columns):
    for rowIndex in range(Rows):
        print(matrix[rowIndex][colIndex], end = " ")
    print()

# print leading diagonal
for i in range(Rows):
    for j in range(Columns):
        if i == j:
            print(matrix[i][j], end = " ")
        print()

# Print second diagonal 
for i in range(Rows):
    for j in range(Columns):
        if i+j == 2:
            print(matrix[i][j], end = " ")
        print()


for i in range(Rows):
    print(matrix[i][Columns -1-i], end = " ")
print()

# program for calculating the sum of rows
sum = 0
for i in range(Rows): 
    for j in range(Columns):
        sum == matrix[i][j]
print(sum)

# sum of primary diagonal 
sum = 0
for i in range(Rows):
    sum+=matrix[i][i]
print(sum)

# Sum of secondary diagonal
sum = 0 
for i in range(Rows):
    sum+=matrix[i][Columns-1-i]
print(sum)

