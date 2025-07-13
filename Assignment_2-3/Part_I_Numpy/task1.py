import numpy as np

# 1D array
arr1 = np.arange(1, 11)

# 2D array
arr2 = np.arange(1, 10).reshape(3, 3)

# 3D array
arr3 = np.random.rand(3, 5, 3)

# Shape, size, dtype
print("Array 1:", arr1.shape, arr1.size, arr1.dtype)
print("Array 2:", arr2.shape, arr2.size, arr2.dtype)
print("Array 3:", arr3.shape, arr3.size, arr3.dtype)