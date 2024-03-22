from sklearn.linear_model import LinearRegression
import numpy as np
 
X = np.array([[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]])
y = np.array([1, 2, 3, 4])
 
reg = LinearRegression()
 
reg.fit(X, y)
 
print(reg.coef_)