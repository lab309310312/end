"""
Experiment 9: Hyperparameter tuning using GridSearchCV / RandomizedSearchCV
Dataset: synthetic classification data created in the program.
"""
import os, time
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import randint, uniform
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split, GridSearchCV, RandomizedSearchCV, StratifiedKFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report

os.makedirs("output", exist_ok=True)
X, y = make_classification(n_samples=800, n_features=12, n_informative=6, n_redundant=2,
                           flip_y=0.05, random_state=21)
pd.DataFrame(X).assign(target=y).to_csv("output/tuning_dataset.csv", index=False)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25, stratify=y, random_state=1)
cv = StratifiedKFold(5, shuffle=True, random_state=0)

# ---------- Baseline ----------
base = RandomForestClassifier(random_state=0).fit(Xtr, ytr)
print(f"Baseline RandomForest test acc: {base.score(Xte, yte):.3f}")

# ---------- GridSearchCV on SVM ----------
print("\n=== GridSearchCV (SVM) ===")
pipe = Pipeline([("sc", StandardScaler()), ("svm", SVC())])
grid = {"svm__C": [0.1, 1, 10, 100], "svm__gamma": [0.001, 0.01, 0.1, 1], "svm__kernel": ["rbf", "linear"]}
t = time.time()
gs = GridSearchCV(pipe, grid, cv=cv, scoring="accuracy", n_jobs=-1).fit(Xtr, ytr)
print(f"Time: {time.time()-t:.1f}s | combinations tried: {len(gs.cv_results_['params'])}")
print("Best params:", gs.best_params_)
print(f"Best CV acc: {gs.best_score_:.3f} | Test acc: {gs.score(Xte, yte):.3f}")

res = pd.DataFrame(gs.cv_results_)
rbf = res[res["param_svm__kernel"] == "rbf"].pivot_table(
    index="param_svm__C", columns="param_svm__gamma", values="mean_test_score")
plt.figure(figsize=(6, 4)); sns.heatmap(rbf.astype(float), annot=True, fmt=".3f", cmap="YlGnBu")
plt.title("GridSearch: RBF SVM CV accuracy"); plt.xlabel("gamma"); plt.ylabel("C")
plt.tight_layout(); plt.savefig("output/exp9_grid_heatmap.png", dpi=120); plt.close()

# ---------- RandomizedSearchCV on Random Forest ----------
print("\n=== RandomizedSearchCV (Random Forest) ===")
dist = {"n_estimators": randint(50, 400), "max_depth": randint(2, 20),
        "min_samples_split": randint(2, 20), "min_samples_leaf": randint(1, 10),
        "max_features": uniform(0.2, 0.7)}
t = time.time()
rs = RandomizedSearchCV(RandomForestClassifier(random_state=0), dist, n_iter=25, cv=cv,
                        scoring="accuracy", n_jobs=-1, random_state=0).fit(Xtr, ytr)
print(f"Time: {time.time()-t:.1f}s | candidates sampled: 25")
print("Best params:", rs.best_params_)
print(f"Best CV acc: {rs.best_score_:.3f} | Test acc: {rs.score(Xte, yte):.3f}")
print(classification_report(yte, rs.predict(Xte)))

# ---------- Comparison ----------
summary = pd.DataFrame({
    "Model": ["RF default", "SVM GridSearch", "RF RandomSearch"],
    "Test accuracy": [base.score(Xte, yte), gs.score(Xte, yte), rs.score(Xte, yte)]}).round(3)
print(summary)
summary.plot(x="Model", y="Test accuracy", kind="bar", legend=False, ylim=(0.5, 1.0), rot=0)
plt.title("Effect of hyperparameter tuning"); plt.savefig("output/exp9_comparison.png", dpi=120); plt.close()
