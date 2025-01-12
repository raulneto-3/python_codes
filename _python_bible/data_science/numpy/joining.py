import numpy as np
# np.concatenate((a, b), axis=0): Join a sequence of arrays along an existing axis.
# np.stack(a, b): Join a sequence of arrays along a new axis.
# np.hstack((a, b)): Stack arrays in sequence horizontally (column wise).
# np.vstack((a, b)): Stack arrays in sequence vertically (row wise).

a = np.array([10, 20, 30])
b = np.array([20, 20, 10])

print(np.concatenate((a, b), axis=0))
print(np.stack((a, b), axis=0))


