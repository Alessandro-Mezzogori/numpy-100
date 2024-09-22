import numpy as np

arr = np.ones(3)
arr = np.pad(arr[np.newaxis,:], 1, mode='constant', constant_values=0)

print(arr)