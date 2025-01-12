import numpy as np
# np.resize(a, new_shape): Return a new array with the specified shape.
# np.append(a, values, axis=None): Append values to the end of an array.
# np.insert(a, index, values, axis=None): Insert values along the given axis before the given index.
# np.delete(a, index, axis=None): Return a new array with sub-arrays along an axis deleted.

a = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90],
    [100, 110, 120]
])
np.save('python_bible/data_science/numpy/adding_and_removing.npy', a)
b = np.load('python_bible/data_science/numpy/adding_and_removing.npy')
print(b)