#### 42. Consider two random array A and B, check if they are equal (★★☆)

import numpy as np

A = np.random.rand(5)
B = np.random.rand(5)

print(A, B, np.allclose(A,B))
print(A, B, np.array_equal(A,B))


