import numpy as np

arr = np.arange(1, 13)
reshaped_2d = arr.reshape(4, 3)
reshaped_3d = arr.reshape(2, 2, 3)
transposed = reshaped_2d.T

print("2D Reshape:", reshaped_2d)
print("3D Reshape:", reshaped_3d)
print("Transposed:", transposed, "Shape:", transposed.shape)