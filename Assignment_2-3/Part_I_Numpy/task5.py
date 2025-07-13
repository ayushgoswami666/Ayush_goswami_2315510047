import numpy as np

arr = np.random.randint(10, 51, 15)

print("Original:", arr)
print("Greater than 25:", arr[arr > 25])
arr[arr < 30] = 0
print("After replacing <30 with 0:", arr)
print("Divisible by 5 count:", np.sum(arr % 5 == 0))