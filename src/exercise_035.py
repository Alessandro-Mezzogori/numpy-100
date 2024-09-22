import numpy as np

A = np.ones(5) * 1
B = np.ones(5) * 2

print("A", A)
print("B", B)
np.add(A,B, out=B)
print("A+B", B)

np.divide(A,-2, out=A)
print("-A/2", A)

np.multiply(A,B, out=A)
print(A)
