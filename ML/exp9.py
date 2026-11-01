from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV

x, y = load_iris(return_X_y=True)

model = DecisionTreeClassifier()

params = {
    'max_depth': [2, 3, 4, 5],
    'criterion': ['gini', 'entropy']
}

grid = GridSearchCV(model, params, cv=5)
grid.fit(x, y)

print("Grid Best Parameters:", grid.best_params_)
print("Grid Best Score:", grid.best_score_)

random = RandomizedSearchCV(model, params, cv=5, n_iter=4, random_state=0)
random.fit(x, y)

print("Random Best Parameters:", random.best_params_)
print("Random Best Score:", random.best_score_)