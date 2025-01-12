import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,50,100)
y = np.sin(x)
plt.title("Sine Function")
plt.suptitle("Data Science")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.grid(True)
plt.plot(x,y)
plt.show()
