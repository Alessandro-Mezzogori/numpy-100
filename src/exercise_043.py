#### 43. Make an array immutable (read-only) (★★☆)

import numpy as np

arr = np.arange(5)
arr.setflags(write=False)

arr[1] = 2
