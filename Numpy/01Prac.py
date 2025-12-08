import numpy as np

arr = np.array((1,2,3,4,5))
print(arr)
print(type(arr))

# creating matrices zeros
zero = np.zeros((2,3))
print(zero)

# creatng matrices one
one = np.ones((2,3))
print(one)

#creating matrices with range 
#np.arrange(start, end, interval/gap)
in_range = np.arange(1, 10, 2)
print(in_range)

#linspace array
#gives an range between 2 number with given interval/gap 
#np.linspace(start, end, interval/gap)
linspace = np.linspace(1, 10, 5)
print(linspace)