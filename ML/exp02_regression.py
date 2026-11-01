"""
Experiment 2: Simple, Multiple and Logistic Regression + performance assessment
Datasets: synthetic house-price data (regression) and synthetic diabetes-risk data (logistic).
"""
import os
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (mean_absolute_error, mean_squared_error, r2_score,
                             accuracy_score, precision_score, recall_score, f1_score,
                             confusion_matrix, classification_report, roc_curve, roc_auc_score)

os.makedirs("output", exist_ok=True)
rng = np.random.default_rng(0)

# -------- Create dataset 1: house prices --------
n = 300
house = pd.DataFrame({
    "area_sqft": rng.normal(1500, 400, n).clip(500, 3500),
    "bedrooms": rng.integers(1, 6, n),
    "age_years": rng.integers(0, 40, n),
    "dist_city_km": rng.uniform(1, 30, n),
})
house["price_lakh"] = (10 + 0.05 * house["area_sqft"] + 5 * house["bedrooms"]
                       - 0.4 * house["age_years"] - 0.8 * house["dist_city_km"]
                       + rng.normal(0, 8, n))
house.to_csv("output/house_prices.csv", index=False)

def report(y_true, y_pred, name):
    mse = mean_squared_error(y_true, y_pred)
    print(f"{name}: MAE={mean_absolute_error(y_true, y_pred):.2f}  MSE={mse:.2f}  "
          f"RMSE={np.sqrt(mse):.2f}  R2={r2_score(y_true, y_pred):.3f}")

# -------- Simple linear regression --------
print("=== SIMPLE LINEAR REGRESSION (area -> price) ===")
X = house[["area_sqft"]]; y = house["price_lakh"]
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=1)
slr = LinearRegression().fit(Xtr, ytr)
print(f"Equation: price = {slr.intercept_:.2f} + {slr.coef_[0]:.4f} * area")
report(yte, slr.predict(Xte), "Simple LR")
plt.scatter(Xte, yte, label="actual"); plt.plot(Xte.sort_values("area_sqft"),
    slr.predict(Xte.sort_values("area_sqft")), "r", label="fit")
plt.xlabel("area"); plt.ylabel("price"); plt.legend(); plt.title("Simple Linear Regression")
plt.savefig("output/exp2_simple_lr.png", dpi=120); plt.close()

# -------- Multiple linear regression --------
print("\n=== MULTIPLE LINEAR REGRESSION ===")
X = house.drop(columns="price_lakh"); y = house["price_lakh"]
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=1)
mlr = LinearRegression().fit(Xtr, ytr)
print("Intercept:", round(mlr.intercept_, 2))
print(pd.Series(mlr.coef_, index=X.columns).round(4))
pred = mlr.predict(Xte)
report(yte, pred, "Multiple LR")
plt.scatter(yte, pred); plt.plot([yte.min(), yte.max()], [yte.min(), yte.max()], "r--")
plt.xlabel("Actual"); plt.ylabel("Predicted"); plt.title("Multiple LR: actual vs predicted")
plt.savefig("output/exp2_multiple_lr.png", dpi=120); plt.close()

# -------- Create dataset 2: diabetes risk (binary) --------
m = 500
d = pd.DataFrame({
    "glucose": rng.normal(120, 30, m),
    "bmi": rng.normal(28, 6, m),
    "age": rng.integers(21, 80, m),
    "bp": rng.normal(75, 12, m),
})
z = -12 + 0.045 * d["glucose"] + 0.08 * d["bmi"] + 0.03 * d["age"] + 0.01 * d["bp"]
d["diabetic"] = (rng.random(m) < 1 / (1 + np.exp(-z))).astype(int)
d.to_csv("output/diabetes_synthetic.csv", index=False)

print("\n=== LOGISTIC REGRESSION ===")
X = d.drop(columns="diabetic"); y = d["diabetic"]
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25, stratify=y, random_state=1)
sc = StandardScaler().fit(Xtr)
clf = LogisticRegression().fit(sc.transform(Xtr), ytr)
yp = clf.predict(sc.transform(Xte)); prob = clf.predict_proba(sc.transform(Xte))[:, 1]
print(f"Accuracy={accuracy_score(yte, yp):.3f} Precision={precision_score(yte, yp):.3f} "
      f"Recall={recall_score(yte, yp):.3f} F1={f1_score(yte, yp):.3f} AUC={roc_auc_score(yte, prob):.3f}")
print("Confusion matrix:\n", confusion_matrix(yte, yp))
print(classification_report(yte, yp))
fpr, tpr, _ = roc_curve(yte, prob)
fig, ax = plt.subplots(1, 2, figsize=(10, 4))
sns.heatmap(confusion_matrix(yte, yp), annot=True, fmt="d", cmap="Blues", ax=ax[0]); ax[0].set_title("Confusion matrix")
ax[1].plot(fpr, tpr, label=f"AUC={roc_auc_score(yte, prob):.2f}"); ax[1].plot([0, 1], [0, 1], "k--")
ax[1].set(title="ROC curve", xlabel="FPR", ylabel="TPR"); ax[1].legend()
plt.tight_layout(); plt.savefig("output/exp2_logistic.png", dpi=120); plt.close()
