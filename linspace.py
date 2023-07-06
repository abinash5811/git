# import numpy as np
# # arr=np.linspace(1,100,100)
# # print(arr)
# # arr1=arr.reshape(10,10)
# # print(arr1)
# # arr2=np.arange(1,101,10)
# # print(arr2)
# matrix=np.zeros((10,10))
# matrix[0, 0] = 1
# matrix[0, 9] = 100
# matrix[9, 0] = 50
# row_interval=(100-1)/8
# col_interval=(50-1)/8
# # print(row_interval)
# # print(col_interval)
# for i in range(1, 9):
#     matrix[0, i] = matrix[0, i-1] + row_interval
#     matrix[i, 0] = matrix[i-1, 0] + col_interval

# print(matrix)

import numpy as np

# Create a 10x10 matrix with zeros
matrix = np.zeros((10, 10))

# Set the values based on the given constraints
matrix[0, 0] = 1
matrix[0, 9] = 100
matrix[9, 0] = 50

# Calculate the intervals
row_interval = (100 - 1) / 8
col_interval = (50 - 1) / 8

# Fill in the remaining elements in rows
for i in range(1, 9):
    matrix[0, i] = matrix[0, i-1] + row_interval

# Fill in the remaining elements in columns
for i in range(1, 9):
    matrix[i, 0] = matrix[i-1, 0] + col_interval

# Fill in the remaining elements in the matrix
for i in range(1, 9):
    for j in range(1, 9):
        matrix[i, j] = matrix[i, j-1] + row_interval

# Print the resulting matrix
print(matrix)



