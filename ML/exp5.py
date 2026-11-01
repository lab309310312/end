from sklearn.ensemble import AdaBoostClassifier

x = [[1, 2], [2, 3], [3, 4], [6, 7], [7, 8], [8, 9]]
y = [0, 0, 0, 1, 1, 1]

model = AdaBoostClassifier(n_estimators=50)
model.fit(x, y)

print("Prediction:", model.predict([[5, 6]]))
print("Accuracy:", model.score(x, y))

#xgboost

from xgboost import XGBClassifier

# 1. Data (Using the exact same data)
X = [[0], [1], [2], [3]]
y = [0, 0, 1, 1]

# 2. Train the Model
model = XGBClassifier(n_estimators=10, random_state=0)
model.fit(X, y)

# 3. Print Results
print("\n--- XGBoost ---")
print("Predicted Class for [1.5]:", model.predict([[1.5]])[0])