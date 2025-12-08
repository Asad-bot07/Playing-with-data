import numpy as np

#manipulating an array

array = np.array((1, 2, 3, 4, 5, 6))
print(array)

#reshapes a 1d array to 2d array
new_arr = array.reshape((2,3))
print(new_arr)

#dimensions
expanded = array[:, np.newaxis]
print(expanded)
