import numpy as np

arr = np.array((1, 2, 3, 4, 5, 6, 7, 8, 9))

#indexing - array always start from 0
print(arr[5])
print(arr[-1]) #negative indexing

#slicing an array
print(arr[3:8])
print(arr[::-1])

#reshaping
reshaped = arr.reshape(3,3)
print(reshaped)