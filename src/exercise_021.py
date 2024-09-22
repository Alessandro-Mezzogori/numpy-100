import numpy as np

m = np.zeros(16, dtype=int)
m[:8:2] = 1
m[9::2] = 1
m = np.tile(m, 4).reshape(8,8)
print(m)

print(np.tile(np.array([[0,1],[1,0]]), (4,4)))
