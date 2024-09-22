#### 45. Create random vector of size 10 and replace the maximum value by 0 (★★☆)

import numpy as np

Z = np.random.randint(1, 10, 10)
print(Z)

Z[Z == np.max(Z)] = 0
print(Z)

# soluzione

Z = np.random.randint(1, 10, 10)
print(Z)

# argmax ritorna argomento in modo che si abbia il valore massimo di uan funzione
# nel caso di un array restituisce l'indice corrispondente al valore maggiore
Z[Z.argmax()] = 0
print(Z)
