import numpy as np

arr = np.random.rand(5,5)
print((arr - np.mean(arr)) / np.std(arr))