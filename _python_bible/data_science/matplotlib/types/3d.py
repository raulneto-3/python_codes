import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

z = np.linspace(0, 20, 100)
x = np.sin(z)
y = np.cos(z)
ax = plt.axes(projection='3d')
ax.plot3D(x, y, z)
plt.show()