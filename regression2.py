import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
# generate random data-set
np.random.seed(0)
x = np.random.rand(100, 1)
y = 2 + 3 * x + np.random.rand(100, 1)
 
regression_model = LinearRegression()
 
regression_model.fit(x, y)
 
y_predicted = regression_model.predict(x)
 
rmse = mean_squared_error(y, y_predicted)
r2 = r2_score(y, y_predicted)
 
print('Slope:' ,regression_model.coef_)
print('Intercept:', regression_model.intercept_)
print('Root mean squared error: ', rmse)
print('R2 score: ', r2)

 
plt.scatter(x, y, s=10)
plt.xlabel('x')
plt.ylabel('y')
 
plt.plot(x, y_predicted, color='r')
plt.show()