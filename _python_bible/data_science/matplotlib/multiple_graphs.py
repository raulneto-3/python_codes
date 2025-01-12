import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 5, 200)
y1 = 2 * x
y2 = x**2
y3 = np.log(x)
plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)
plt.show()