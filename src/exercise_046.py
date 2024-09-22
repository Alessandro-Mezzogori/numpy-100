#### 46. Create a structured array with `x` and `y` coordinates covering the [0,1]x[0,1] area (★★☆)
# Create a structured array with `x` and `y` coordinates
# covering the [0,1]x[0,1] area (★★☆)

import numpy as np


Z = np.zeros((6,6), dtype=[('x', float), ('y', float)])
Z['x'], Z['y'] = np.meshgrid(np.linspace(0, 1, Z.shape[0]), np.linspace(0,1, Z.shape[1]))

print(Z)

