from sklearn.tree import DecisionTreeClassifier

# 1. Provide Data (Features and Labels)
# Example: 2 features per sample
X = [[0, 0], [1, 1], [2, 2], [3, 3]] 
y = [0, 0, 1, 1]                     # Class labels (0 or 1)

# 2. Train the Model
model = DecisionTreeClassifier()
model.fit(X, y)

# 3. Print Results
test_data = [[1.5, 1.5]]
print("--- Decision Tree Classifier ---")
print("Predicted Class for", test_data, ":", model.predict(test_data)[0])