import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

x = [[1, 2], [2, 3], [3, 2], [8, 8], [9, 8], [8, 9]]

model = KMeans(n_clusters=2, random_state=0, n_init=10)
model.fit(x)

print("Clusters:", model.labels_)
print("Centroids:", model.cluster_centers_)

plt.scatter([i[0] for i in x], [i[1] for i in x],
            c=model.labels_)

plt.scatter(model.cluster_centers_[:, 0],
            model.cluster_centers_[:, 1],
            marker='X', s=200)

plt.show()