from sklearn.svm import SVC

x = [[1, 2], [2, 3], [3, 4], [6, 7], [7, 8], [8, 9]]
y = [0, 0, 0, 1, 1, 1]

model = SVC()
model.fit(x, y)

print("Prediction:", model.predict([[5, 6]]))


# SVM for Regression

from sklearn.svm import SVR

x = [[1], [2], [3], [4], [5]]
y = [2, 4, 6, 8, 10]

model = SVR()
model.fit(x, y)

print("Prediction:", model.predict([[6]]))

# SVM for Outlier Detection

from sklearn.svm import OneClassSVM

# 1. Data (Only X is needed - finding abnormal data points)
X_train = [[1], [1.1], [1.2], [1.1]] 

# 2. Train and Predict (1 = Normal, -1 = Outlier)
model = OneClassSVM(gamma='auto')
model.fit(X_train) 

test_data = [[1.15], [9.9]] # 9.9 is an obvious outlier

print("\n--- SVM Outlier Detection ---")
print("Predictions (1=Normal, -1=Outlier):", model.predict(test_data))