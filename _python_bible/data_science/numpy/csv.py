import numpy as np

a = np.load('python_bible/data_science/numpy/adding_and_removing.npy')
np.savetxt('python_bible/data_science/numpy/converting_to_csv.csv', a)
b = np.loadtxt('python_bible/data_science/numpy/converting_to_csv.csv')
print(b)
c = np.loadtxt('python_bible/data_science/numpy/converting_to_csv.csv', delimiter=';')
