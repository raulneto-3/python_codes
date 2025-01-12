import numpy as np
import matplotlib.pyplot as plt

ax = plt.axes(projection='3d')

def z_function(x, y):
    return np.sin(np.sqrt(x**2 + y**2)) 

x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)

X, Y = np.meshgrid(x, y)
Z = z_function(X, Y)

ax.plot_surface(X, Y, Z, cmap='viridis')
plt.show()