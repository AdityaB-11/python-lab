import numpy as np

 
arr_int = np.array([1, 2, 3], dtype=np.int32)
arr_float = np.array([1.0, 2.0, 3.0], dtype=np.float64)

 
print(arr_int.dtype)
print(arr_float.dtype)

 
arr_custom = np.array([1, 2, 3], dtype=np.uint16)

print(arr_custom)