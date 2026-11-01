"""
Experiment 6: K-Means Clustering
Dataset: synthetic mall-customer data (annual income vs spending score) created in the program.
"""
import os
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score, davies_bouldin_score

os.makedirs("output", exist_ok=True)
rng = np.random.default_rng(11)
centers = [(25, 80), (25, 20), (55, 50), (85, 82), (85, 18)]     # (income k$, spending score)
data = np.vstack([rng.normal(c, 6, (60, 2)) for c in centers])
df = pd.DataFrame(data, columns=["annual_income", "spending_score"]).clip(lower=1)
df.insert(0, "customer_id", range(1, len(df) + 1))
df.to_csv("output/mall_customers.csv", index=False)

X = StandardScaler().fit_transform(df[["annual_income", "spending_score"]])

# ---- Elbow + silhouette to choose K ----
ks = range(2, 10)
inertia, sil = [], []
for k in ks:
    km = KMeans(n_clusters=k, n_init=10, random_state=0).fit(X)
    inertia.append(km.inertia_); sil.append(silhouette_score(X, km.labels_))
    print(f"K={k}: inertia={km.inertia_:.1f}  silhouette={sil[-1]:.3f}")
best_k = list(ks)[int(np.argmax(sil))]
print("Best K by silhouette:", best_k)

fig, ax = plt.subplots(1, 2, figsize=(10, 4))
ax[0].plot(ks, inertia, "o-"); ax[0].set(title="Elbow method", xlabel="K", ylabel="Inertia (WCSS)")
ax[1].plot(ks, sil, "s-g"); ax[1].set(title="Silhouette score", xlabel="K")
plt.tight_layout(); plt.savefig("output/exp6_elbow.png", dpi=120); plt.close()

# ---- Final model ----
km = KMeans(n_clusters=best_k, init="k-means++", n_init=10, random_state=0).fit(X)
df["cluster"] = km.labels_
print("\nDavies-Bouldin index:", round(davies_bouldin_score(X, km.labels_), 3))
print("\nCluster profile:\n", df.groupby("cluster")[["annual_income", "spending_score"]].agg(["mean", "count"]).round(1))

cent = StandardScaler().fit(df[["annual_income", "spending_score"]]).inverse_transform(km.cluster_centers_)
plt.figure(figsize=(7, 5))
plt.scatter(df["annual_income"], df["spending_score"], c=df["cluster"], cmap="tab10", s=25)
plt.scatter(cent[:, 0], cent[:, 1], c="k", marker="X", s=200, label="centroids")
plt.xlabel("Annual income (k$)"); plt.ylabel("Spending score"); plt.legend(); plt.title(f"K-Means (K={best_k})")
plt.savefig("output/exp6_clusters.png", dpi=120); plt.close()

# predict for new customers
new = pd.DataFrame([[30, 75], [90, 15]], columns=["annual_income", "spending_score"])
sc = StandardScaler().fit(df[["annual_income", "spending_score"]])
print("\nNew customers ->", km.predict(sc.transform(new)))
