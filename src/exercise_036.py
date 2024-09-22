import numpy as np

Z = np.random.uniform(0, 10, 10)
print(Z)

print("Floor", np.floor(Z))
print("Sub floating", Z - Z%1)
print("Truncate", np.trunc(Z))
print("Cast", Z.astype(int))
print("Quotient", Z // 1)
