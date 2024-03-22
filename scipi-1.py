from scipy import linalg
import numpy as np
my_arr = np.array([[5,7],[11,3]])
eg_val, eg_vect = linalg.eig(my_arr)
print("The Eigenvalues are :")
print(eg_val)
print("The Eigenvectors are :")
print(eg_vect)