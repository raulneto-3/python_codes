import numpy as np
import matplotlib.pyplot as plt

#       Styles
## https://bit.ly/2JfhJ4o
# from matplotlib import style
# style.use('ggplot')

x = np.linspace(0, 20, 100)
y = np.sin(x)
plt.plot(x, y)
plt.show()

xx = np.linspace(0, 10, 100)
yy = (6 * xx - 30)**2
plt.plot(xx, yy)
plt.show()