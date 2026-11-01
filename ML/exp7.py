from sklearn.decomposition import PCA

# 1. Data (High Dimensional: 3 Features/Dimensions)
X = [[1, 2, 3], 
     [2, 4, 6], 
     [3, 6, 9], 
     [4, 8, 12]]

# 2. Train and Reduce (Reduce down to 2 Features/Dimensions)
pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X)

# 3. Print Results
print("--- PCA Dimensionality Reduction ---")
print("Original shape:", len(X[0]), "dimensions")
print("New shape:", len(X_reduced[0]), "dimensions\n")

print("Reduced Data (2D):")
print(X_reduced)

# Shows how much information (variance) is retained in the new dimensions
print("\nExplained Variance Ratio:", pca.explained_variance_ratio_)