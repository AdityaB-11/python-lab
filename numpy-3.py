import numpy as np

arr1d = np.array([1, 2, 3, 4, 5])
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

 
element = arr1d[2] 
print("Access the element at index 2 : ", element)

 
slice1 = arr1d[1:4]  
print("Slice elements from index 1 to 3 : ", slice1)

slice2 = arr2d[0, 1:3] 
print("Slice elements from the first row, columns 1 to 2 : ", slice2)