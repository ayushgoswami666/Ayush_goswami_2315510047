import numpy as np

A = np.random.randint(1, 21, 5)
B = np.random.randint(1, 21, 5)

print("A:", A)
print("B:", B)
print("Addition:", A + B)
print("Subtraction:", A - B)
print("Multiplication:", A * B)
print("Division:", A / B)
print("Dot product:", np.dot(A, B))
print("Mean of A:", np.mean(A))
print("Median of A:", np.median(A))
print("Std of A:", np.std(A))
print("Variance of A:", np.var(A))
print("Max of B:", np.max(B), "at index", np.argmax(B))
print("Min of B:", np.min(B), "at index", np.argmin(B))