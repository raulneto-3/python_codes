import numpy as np

a = np.array([[4, 2, 9], [8, 3, 2]])

### Shape Manipulation
# a.reshape(x, y): Returns an array containing the same data with a new shape.
# a.flatten(): Returns a copy of the array collapsed into one dimension.
# a.ravel(): Returns a flattened array.
# a.transpose(): Returns a view of the
# a.swapaxes(axis1, axis2): Returns a view of the array with axis1 and axis2 interchanged.
# a.flat: A 1-D iterator over the array.

for i in a.flat:
    print(i)

print(a.flat[5])