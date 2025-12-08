import numpy as np

# generating random matrix
matrix = np.random.randint(1, 51, size=[3,4])
print(matrix)

# filtering data set
matrix[matrix > 25] = 0
print("\n", matrix)

# calculate summary stat
print("Sum : ", np.sum(matrix))
print("Mean : ", np.mean(matrix))
print("Standard deviation : ", np.std(matrix))