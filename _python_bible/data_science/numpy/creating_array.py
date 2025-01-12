import numpy as np 

# Create a 1D array
a = np.array([1, 2, 3])
print(f"1D array: {a}")

# Create a 2D array
b = np.array([[1, 2, 3], [4, 5, 6]])
print(f"2D array: {b}")

# Create a 3D array
c = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(f"3D array: {c}")


# a 3x3x4
d = np.array([
 [[10,20,30,40], [8,8,2,1], [1,1,1,2]],
 [[9, 9, 2, 39], [1,2,3,3], [0,0,3,2]],
 [[12,33,22,1], [22,1,22,2], [0,2,3,1]]], dtype=float)
print(f"3x3x4: {d}")