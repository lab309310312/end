import numpy as np
from sklearn.linear_model import LinearRegression

# 1. Provide Data (1 Feature)
X = np.array([[1], [2], [3], [4], [5]]) # Independent variable
y = np.array([2, 4, 5, 4, 5])           # Dependent variable

# 2. Train the Model
model = LinearRegression()
model.fit(X, y)

# 3. Print Results
print("--- Simple Linear Regression ---")
print("Coefficient:", model.coef_[0])
print("Intercept:", model.intercept_)
print("Prediction for X=6:", model.predict([[6]])[0])


#2. Multiple Linear Regression

import numpy as np
from sklearn.linear_model import LinearRegression

x = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]])
y = np.array([5, 8, 11, 14, 17])

model = LinearRegression()
model.fit(x, y)

print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)
print("Prediction:", model.predict([[6, 7]]))