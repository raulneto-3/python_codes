import numpy as np

# Full: Return a new array of given shape and type, filled with fill_value.
a = np.full((3,5,4), 7)

# Ones: Return a new array of given shape and type, filled with ones.
b = np.ones((3,5,4))

# Zeros: Return a new array of given shape and type, filled with zeros.
c = np.zeros((3,5,4))

# Empty: Return a new array of given shape and type, without initializing entries.
d = np.empty((3,5,4))

# Random: Return a new array of given shape and type, filled with random values.
e = np.random.random((3,5,4))

# Range: Return evenly spaced values within a given interval.
f = np.arange(0, 100, 2)

# Linspace: Return evenly spaced numbers over a specified interval.
g = np.linspace(0, 100, 10)

