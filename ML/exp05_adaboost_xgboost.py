"""
Experiment 5: AdaBoost classifier & XGBoost algorithm
Dataset: synthetic customer-churn data created in the program.
"""
import os
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, roc_auc_score

try:
    from xgboost import XGBClassifier
    HAVE_XGB = True
except ImportError:                       # pip install xgboost
    from sklearn.ensemble import HistGradientBoostingClassifier as XGBClassifier
    HAVE_XGB = False
    print("xgboost not installed -> using sklearn HistGradientBoosting as stand-in")

os.makedirs("output", exist_ok=True)
X, y = make_classification(n_samples=1000, n_features=8, n_informative=5, n_redundant=1,
                           flip_y=0.05, class_sep=1.0, random_state=5)
cols = ["tenure", "monthly_charge", "support_calls", "usage_hrs", "contract_len",
        "late_payments", "data_gb", "age"]
df = pd.DataFrame(X, columns=cols); df["churn"] = y
df.to_csv("output/churn_synthetic.csv", index=False)

Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25, random_state=2, stratify=y)

# ---------- Baseline ----------
stump = DecisionTreeClassifier(max_depth=1).fit(Xtr, ytr)
print(f"Single decision stump accuracy: {stump.score(Xte, yte):.3f}")

# ---------- AdaBoost ----------
print("\n=== ADABOOST ===")
ada = AdaBoostClassifier(estimator=DecisionTreeClassifier(max_depth=1),
                         n_estimators=100, learning_rate=0.5, random_state=0).fit(Xtr, ytr)
yp = ada.predict(Xte)
print(f"Accuracy={accuracy_score(yte, yp):.3f}  AUC={roc_auc_score(yte, ada.predict_proba(Xte)[:, 1]):.3f}")
print("Confusion matrix:\n", confusion_matrix(yte, yp))
print(classification_report(yte, yp))
print("5-fold CV accuracy:", cross_val_score(ada, X, y, cv=5).mean().round(3))
staged = [accuracy_score(yte, p) for p in ada.staged_predict(Xte)]

# ---------- XGBoost ----------
print("\n=== XGBOOST ===")
if HAVE_XGB:
    xgb = XGBClassifier(n_estimators=200, learning_rate=0.1, max_depth=3, subsample=0.8,
                        colsample_bytree=0.8, eval_metric="logloss", random_state=0)
else:
    xgb = XGBClassifier(max_iter=200, learning_rate=0.1, max_depth=3, random_state=0)
xgb.fit(Xtr, ytr)
yp = xgb.predict(Xte)
print(f"Accuracy={accuracy_score(yte, yp):.3f}  AUC={roc_auc_score(yte, xgb.predict_proba(Xte)[:, 1]):.3f}")
print("Confusion matrix:\n", confusion_matrix(yte, yp))
print(classification_report(yte, yp))

# ---------- Plots ----------
fig, ax = plt.subplots(1, 2, figsize=(11, 4))
ax[0].plot(staged); ax[0].set(title="AdaBoost: accuracy vs #estimators", xlabel="n_estimators", ylabel="test accuracy")
if HAVE_XGB:
    imp = pd.Series(xgb.feature_importances_, index=cols).sort_values()
    imp.plot(kind="barh", ax=ax[1], title="XGBoost feature importance")
plt.tight_layout(); plt.savefig("output/exp5_boosting.png", dpi=120); plt.close()
print("\nAdaBoost vs XGBoost test accuracy: %.3f vs %.3f" % (ada.score(Xte, yte), xgb.score(Xte, yte)))
