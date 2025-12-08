import numpy as np

arr = np.array([[1, 2, 3], [2, 3, 4]])
print(arr)

# sum of the coulumn
sum_column = np.sum(arr, axis=0)
print(sum_column)

# sum of the rows
sum_rows = np.sum(arr, axis=1)
print(sum_rows)