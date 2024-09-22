#### 41. How to sum a small array faster than np.sum? (★★☆)

import numpy as np
from time import time

def test(num: int):
    arr = np.random.rand(num)
    start = time()
    np.sum(arr)
    print("\tnp.sort", time() - start)

    start = time()
    np.add.reduce(arr)
    print("\tnp.add.reduce", time() - start)

print('10')
test(10)
print('100')
test(100)
print('1000')
test(1000)
print('10000')
test(10000)
print('100000')
test(100000)
print('1000000')
test(1000000)
print('10000000')
test(10000000)



