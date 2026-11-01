"""
Experiment 4: SVM for classification, regression and outlier detection
Datasets: synthetic (make_moons / noisy sine curve / gaussian blobs with outliers).
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
from sklearn.svm import SVC, SVR, OneClassSVM
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score, classification_report, mean_squared_error, r2_score

os.makedirs("output", exist_ok=True)
rng = np.random.default_rng(1)

def boundary(model, X, y, ax, title):
    xx, yy = np.meshgrid(np.linspace(X[:, 0].min() - .5, X[:, 0].max() + .5, 300),
                         np.linspace(X[:, 1].min() - .5, X[:, 1].max() + .5, 300))
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)
    ax.contourf(xx, yy, Z, alpha=.3, cmap="coolwarm"); ax.scatter(X[:, 0], X[:, 1], c=y, cmap="coolwarm", edgecolor="k", s=20)
    ax.set_title(title)

# ---------- 1. Classification ----------
print("=== SVM CLASSIFICATION ===")
X, y = make_moons(400, noise=0.25, random_state=0)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25, random_state=0)
fig, axs = plt.subplots(1, 3, figsize=(15, 4))
for ax, (kern, kw) in zip(axs, [("linear", {}), ("poly", {"degree": 3}), ("rbf", {"gamma": "scale"})]):
    m = make_pipeline(StandardScaler(), SVC(kernel=kern, C=1.0, **kw)).fit(Xtr, ytr)
    acc = accuracy_score(yte, m.predict(Xte))
    print(f"kernel={kern:6s} test accuracy={acc:.3f}")
    boundary(m, X, y, ax, f"{kern} kernel (acc={acc:.2f})")
plt.tight_layout(); plt.savefig("output/exp4_svc.png", dpi=120); plt.close()
print(classification_report(yte, m.predict(Xte)))
print("Support vectors per class (rbf):", m[-1].n_support_)

# ---------- 2. Regression (SVR) ----------
print("\n=== SVM REGRESSION (SVR) ===")
Xr = np.sort(rng.uniform(0, 5, 200))[:, None]
yr = np.sin(Xr).ravel() + rng.normal(0, 0.15, 200)
plt.scatter(Xr, yr, s=12, c="gray", label="data")
for kern, col in [("linear", "r"), ("poly", "g"), ("rbf", "b")]:
    s = SVR(kernel=kern, C=10, epsilon=0.1).fit(Xr, yr)
    p = s.predict(Xr)
    print(f"{kern:6s} RMSE={np.sqrt(mean_squared_error(yr, p)):.3f}  R2={r2_score(yr, p):.3f}")
    plt.plot(Xr, p, col, label=kern)
plt.legend(); plt.title("SVR with different kernels")
plt.savefig("output/exp4_svr.png", dpi=120); plt.close()

# ---------- 3. Outlier detection (One-Class SVM) ----------
print("\n=== OUTLIER DETECTION (One-Class SVM) ===")
normal = rng.normal(0, 1, (300, 2))
outliers = rng.uniform(-6, 6, (20, 2))
Xo = np.vstack([normal, outliers])
oc = OneClassSVM(kernel="rbf", gamma=0.1, nu=0.07).fit(normal)   # train on normal data
pred = oc.predict(Xo)                                              # +1 inlier, -1 outlier
print("Detected outliers:", (pred == -1).sum(), "| true outliers injected:", len(outliers))
print("Injected outliers caught:", (pred[300:] == -1).sum(), "/ 20")
xx, yy = np.meshgrid(np.linspace(-7, 7, 300), np.linspace(-7, 7, 300))
Z = oc.decision_function(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)
plt.contourf(xx, yy, Z, levels=np.linspace(Z.min(), 0, 7), cmap="Blues_r"); plt.contour(xx, yy, Z, levels=[0], colors="red")
plt.scatter(Xo[pred == 1, 0], Xo[pred == 1, 1], c="g", s=15, label="inlier")
plt.scatter(Xo[pred == -1, 0], Xo[pred == -1, 1], c="k", marker="x", label="outlier"); plt.legend()
plt.title("One-Class SVM"); plt.savefig("output/exp4_outlier.png", dpi=120); plt.close()
