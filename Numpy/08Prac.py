import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

print("Sum of the array : ", np.sum(arr))
print("Mean : ", np.mean(arr))
print("Max : ", np.max(arr))
print("Min : ", np.min(arr))
print("Standard deviation : ", np.std(arr))
print("Sum of rows : ", np.sum(arr, axis=1))