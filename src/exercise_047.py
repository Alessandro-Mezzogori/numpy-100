#### 47. Given two arrays, X and Y, construct the Cauchy matrix C (Cij =1/(xi - yj)) (★★☆)

import numpy as np

X = np.random.randint(0, 10, 10).reshape(1,10)
Y = np.random.randint(0, 10, 10).reshape(1,10)

# versione sbagliata
print(X)
print(Y)
print("mine", 1 / (X - Y.T))
print("subouter", 1 / np.subtract.outer(X, Y))

# versione giusta
# np.subtract.outer => effettua l'operazione tra tutte le coppie che si possono creare tra X e Y
print(np.allclose(1 / (X - Y.T), (1 / np.subtract.outer(X, Y))))

