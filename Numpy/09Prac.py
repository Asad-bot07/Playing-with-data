import numpy as np

# boolean indexing means creating a boolean array using conditions and use that boolean array to pick only those element where the value is true

arr = np.array([[1, 2, 3], [5, 7, 9]])

evens = arr[arr % 2 == 0] 
print(evens)

arr[arr > 3] = 0
print("Modified array : ", arr)