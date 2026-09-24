# nums = [1,2,3],[1,-18,9],[1,-52,6]
# row = len(nums)
# column = len(nums[0])
# for i in range (0,row):
#     for j in range(0, column):
#         print(nums[i][j], end=" ")
# print()

# Matrix
# nums = [1,2,3] #array

# matrix = [[1,2,4], [4,5,6], [7,8,9]] #Collection of array os a matrix
row = int(input("Enter the value of rows required: "))
column = int(input("Enter the value of columns required: "))
matrix = []

for i in range(row):
    row = []
    for j in range(column):
        value = int(input("Enter value for position ((i), (j)): ")) 
        row.append(value)
    matrix.append(row)

print("Matrix: ")
for r in matrix:  
    print(r)
