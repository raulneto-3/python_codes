import numpy as np
# np.split(a, x, axis=0): Split an array into multiple sub-arrays.
# np.hspli(a, x): Split an array into multiple sub-arrays horizontally (column-wise).
# np.vsplit(a, x): Split an array into multiple sub-arrays vertically (row-wise).
a = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90],
    [100, 110, 120]
])

print(np.split(a, 2, axis=0))
print(np.split(a, 4, axis=1))