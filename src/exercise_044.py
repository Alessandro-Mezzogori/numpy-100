#### 44. Consider a random 10x2 matrix representing cartesian coordinates, convert them to polar coordinates (★★☆)

import numpy as np

M = np.random.rand(10, 2)
print(M)

X = M[:, 0]
Y = M[:, 1]

R = np.sqrt(X**2 + Y**2).reshape(10, 1)
T = np.atan2(X,Y).reshape(10, 1)

print(np.concat((R,T), axis=1))
