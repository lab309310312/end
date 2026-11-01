"""
Experiment 7: PCA for Dimensionality Reduction
Dataset: synthetic 10-feature data with correlated features and 3 classes, created in the program.
"""
import os
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import make_classification
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

os.makedirs("output", exist_ok=True)
X, y = make_classification(n_samples=500, n_features=10, n_informative=3, n_redundant=5,
                           n_classes=3, n_clusters_per_class=1, class_sep=2.0, random_state=4)
cols = [f"f{i+1}" for i in range(10)]
df = pd.DataFrame(X, columns=cols); df["target"] = y
df.to_csv("output/pca_dataset.csv", index=False)
print("Original shape:", X.shape)

Xs = StandardScaler().fit_transform(X)           # PCA needs scaled data

# ---- Full PCA: explained variance ----
pca = PCA().fit(Xs)
ev = pca.explained_variance_ratio_; cum = ev.cumsum()
print("Explained variance ratio:", ev.round(3))
print("Cumulative:", cum.round(3))
n95 = int(np.argmax(cum >= 0.95) + 1)
print("Components needed for 95% variance:", n95)

fig, ax = plt.subplots(1, 2, figsize=(11, 4))
ax[0].bar(range(1, 11), ev); ax[0].set(title="Scree plot", xlabel="PC", ylabel="Explained variance ratio")
ax[1].plot(range(1, 11), cum, "o-"); ax[1].axhline(.95, color="r", ls="--")
ax[1].set(title="Cumulative variance", xlabel="# components")
plt.tight_layout(); plt.savefig("output/exp7_variance.png", dpi=120); plt.close()

# ---- 2-D projection ----
Z = PCA(n_components=2).fit_transform(Xs)
plt.figure(figsize=(6, 5)); sns.scatterplot(x=Z[:, 0], y=Z[:, 1], hue=y, palette="Set1")
plt.title("Data projected to 2 principal components"); plt.xlabel("PC1"); plt.ylabel("PC2")
plt.savefig("output/exp7_projection.png", dpi=120); plt.close()

# ---- Loadings ----
p2 = PCA(n_components=2).fit(Xs)
load = pd.DataFrame(p2.components_.T, index=cols, columns=["PC1", "PC2"])
print("\nLoadings:\n", load.round(3))
plt.figure(figsize=(4, 5)); sns.heatmap(load, annot=True, cmap="coolwarm"); plt.title("Loadings")
plt.tight_layout(); plt.savefig("output/exp7_loadings.png", dpi=120); plt.close()

# ---- Effect on a classifier ----
Xtr, Xte, ytr, yte = train_test_split(Xs, y, test_size=0.25, random_state=0, stratify=y)
acc_full = LogisticRegression(max_iter=1000).fit(Xtr, ytr).score(Xte, yte)
pc = PCA(n_components=n95).fit(Xtr)
acc_pca = LogisticRegression(max_iter=1000).fit(pc.transform(Xtr), ytr).score(pc.transform(Xte), yte)
print(f"\nAccuracy with all 10 features: {acc_full:.3f}")
print(f"Accuracy with {n95} PCs        : {acc_pca:.3f}")
rec = pc.inverse_transform(pc.transform(Xte))
print("Reconstruction MSE:", round(((Xte - rec) ** 2).mean(), 4))
