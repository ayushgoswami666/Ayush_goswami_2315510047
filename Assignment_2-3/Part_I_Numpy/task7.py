import numpy as np
import time

A = np.random.rand(100, 100)
B = np.random.rand(100, 100)

start = time.time()
C = np.dot(A, B)
end = time.time()

try:
    det = np.linalg.det(C)
    inv = np.linalg.inv(C)
except np.linalg.LinAlgError:
    det = "Not computable"
    inv = "Not invertible"

print("Time taken:", end - start)
print("Determinant:", det)
print("Inverse status:", "Computed" if isinstance(inv, np.ndarray) else inv)