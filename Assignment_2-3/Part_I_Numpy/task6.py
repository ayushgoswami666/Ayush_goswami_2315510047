import numpy as np

equally_spaced = np.linspace(0, 1, 10)
identity = np.eye(4)
rand_arr = np.random.randint(1, 101, 20)
sorted_arr = np.sort(rand_arr)
largest_5 = sorted_arr[-5:]

print("Equally spaced:", equally_spaced)
print("Identity matrix:", identity)
print("Sorted array:", sorted_arr)
print("5 largest:", largest_5)