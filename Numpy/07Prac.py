import numpy as np

# bradcasting : it allows numpy to perform arithmetic operations of diff shapes, smaller array matches the dimension of the larger array

arr = np.array([[1, 2, 3]])
print(arr)
print(arr + 10)

matrix = np.array([[1, 2, 3], [4, 5, 6]])
vector = np.array([9, 6 , 8])
print(matrix + vector)