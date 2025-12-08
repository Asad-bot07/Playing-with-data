import numpy as np

# random seeding
np.random.seed(24)

# from 0 to 1
random_array = np.random.rand(3, 4)
print(random_array)

# real numbers
random_integers = np.random.randint(0, 10, size=[2, 3])
print(random_integers)
