import numpy as np

# Mia soluzione
arr = (np.eye(4) * np.arange(1,5))
arr = np.concat((np.zeros((1,4)), arr), axis=0)
arr = np.concat((arr, np.zeros((5,1))), axis=1)
print(arr)

# Soluzeion
print(np.diag(1 + np.arange(4), k=-1))