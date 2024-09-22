import numpy as np

arr = np.random.uniform(-10, 10, 5)
print(arr)

# valore assoluto in modo che ceil funzioni lontano dallo zero
arr2 = np.abs(arr)
print(arr2)

# ceil per arrotondare verso l'alto
arr2 = np.ceil(arr2)
print(arr2)

# copysign ripristina il segno originale
arr2 = np.copysign(arr2, arr)
print(arr2)