import numpy as np
import matplotlib.pyplot as plt

mu, sigma = 172, 4
x = mu + sigma * np.random.randn(10000)

plt.hist(x, 100, density=True, facecolor='b')
plt.xlabel('Height')
plt.ylabel('Probability')
plt.title('Histogram of Height')
plt.text(160, 0.125,"µ = 172, σ = 4")
plt.axis([155,190,0,0.15])
plt.grid(True)
plt.show()