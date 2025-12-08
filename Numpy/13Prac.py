import numpy as np

# seeding value
np.random.seed(24)

# generating a array with random numbers
matrix = np.random.randint(1, 100, size=[5, 5])
print(matrix)

# printing stats column wise
column_mean = np.mean(matrix, axis=0)
column_std = np.std(matrix, axis=0)
column_sum = np.sum(matrix, axis=0)
print("mean of the column : ",column_mean)
print("sum of the column : ",column_sum)
print("std of the column : ",column_std)

# row wise stats
rows_mean = np.mean(matrix, axis=1)
rows_sum = np.sum(matrix, axis=1)
rows_std = np.std(matrix, axis=1)
print("mean of the rows : ", rows_mean)
print("sum of the rows : ", rows_sum)
print("std of the rows : ", rows_std)