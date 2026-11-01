"""
Experiment 3: Decision Tree (classification + regression)
Dataset: synthetic loan-approval data created in the program.
"""
import os
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor, plot_tree, export_text
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, mean_squared_error, r2_score

os.makedirs("output", exist_ok=True)
rng = np.random.default_rng(7)
n = 600
df = pd.DataFrame({
    "income": rng.normal(50, 15, n).clip(10, 120),        # in thousands
    "credit_score": rng.normal(650, 70, n).clip(300, 850),
    "loan_amount": rng.normal(20, 8, n).clip(2, 60),
    "employed": rng.integers(0, 2, n),
})
score = (0.04 * df["income"] + 0.01 * (df["credit_score"] - 600) - 0.05 * df["loan_amount"]
         + 0.8 * df["employed"] + rng.normal(0, 0.5, n))
df["approved"] = (score > np.median(score)).astype(int)
df.to_csv("output/loan_data.csv", index=False)

X = df.drop(columns="approved"); y = df["approved"]
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25, random_state=3, stratify=y)

print("=== CLASSIFICATION TREE ===")
for crit in ["gini", "entropy"]:
    t = DecisionTreeClassifier(criterion=crit, max_depth=4, random_state=0).fit(Xtr, ytr)
    print(f"criterion={crit}: train acc={t.score(Xtr, ytr):.3f}, test acc={t.score(Xte, yte):.3f}")

tree = DecisionTreeClassifier(criterion="gini", max_depth=4, random_state=0).fit(Xtr, ytr)
yp = tree.predict(Xte)
print("\nConfusion matrix:\n", confusion_matrix(yte, yp))
print(classification_report(yte, yp))
print("Feature importances:\n", pd.Series(tree.feature_importances_, index=X.columns).round(3))
print("\nTree rules:\n", export_text(tree, feature_names=list(X.columns)))

# Overfitting demo
depths = range(1, 15)
tr = [DecisionTreeClassifier(max_depth=d, random_state=0).fit(Xtr, ytr).score(Xtr, ytr) for d in depths]
te = [DecisionTreeClassifier(max_depth=d, random_state=0).fit(Xtr, ytr).score(Xte, yte) for d in depths]
plt.figure(figsize=(6, 4)); plt.plot(depths, tr, label="train"); plt.plot(depths, te, label="test")
plt.xlabel("max_depth"); plt.ylabel("accuracy"); plt.legend(); plt.title("Depth vs accuracy (overfitting)")
plt.savefig("output/exp3_depth_curve.png", dpi=120); plt.close()

plt.figure(figsize=(16, 8))
plot_tree(tree, feature_names=X.columns, class_names=["Rejected", "Approved"], filled=True, fontsize=8)
plt.savefig("output/exp3_tree.png", dpi=120); plt.close()

print("=== REGRESSION TREE (predict loan_amount) ===")
Xr = df[["income", "credit_score", "employed"]]; yr = df["loan_amount"]
Xtr, Xte, ytr, yte = train_test_split(Xr, yr, test_size=0.25, random_state=3)
reg = DecisionTreeRegressor(max_depth=4, random_state=0).fit(Xtr, ytr)
p = reg.predict(Xte)
print(f"RMSE={np.sqrt(mean_squared_error(yte, p)):.2f}  R2={r2_score(yte, p):.3f}")
