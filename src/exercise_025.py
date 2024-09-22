import numpy as np

arr = np.arange(1, 10, dtype=int)
arr[(arr >= 3) & (arr <= 8)] *= -1

print(arr)
