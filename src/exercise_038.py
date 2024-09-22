#### 38. Consider a generator function that generates 10 integers and use it to build an array (★☆☆)
import numpy as np

def generator(num: int):
    for i in range(num):
        yield i

print(np.fromiter(generator(10), int))
