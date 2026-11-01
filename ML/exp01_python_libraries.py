"""
Experiment 1: Study of Python Libraries for ML - NumPy, Pandas, Matplotlib, Seaborn
Dataset: synthetic "students" dataset created in the program.
"""
import os
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")          # remove this line to see plots in a window
import matplotlib.pyplot as plt
import seaborn as sns

os.makedirs("output", exist_ok=True)
rng = np.random.default_rng(42)

# ---------------- NumPy ----------------
print("=" * 20, "NUMPY", "=" * 20)
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.arange(6).reshape(2, 3)
print("a:\n", a, "\nshape:", a.shape, "dtype:", a.dtype)
print("a + b:\n", a + b)
print("a * b (elementwise):\n", a * b)
print("a @ b.T (matrix product):\n", a @ b.T)
print("mean:", a.mean(), "| std:", a.std().round(3), "| col sum:", a.sum(axis=0))
print("linspace:", np.linspace(0, 1, 5))
print("random normal sample:", rng.normal(0, 1, 5).round(3))
print("slicing a[:, 1:] =\n", a[:, 1:])
print("broadcasting a + [10,20,30]:\n", a + np.array([10, 20, 30]))

# ---------------- Pandas ----------------
print("\n" + "=" * 20, "PANDAS", "=" * 20)
n = 200
df = pd.DataFrame({
    "student_id": range(1, n + 1),
    "gender": rng.choice(["M", "F"], n),
    "branch": rng.choice(["CS", "IT", "ENTC", "MECH"], n),
    "study_hours": rng.normal(5, 1.5, n).clip(0, 10).round(1),
    "attendance": rng.normal(80, 10, n).clip(40, 100).round(1),
})
df["marks"] = (35 + 5 * df["study_hours"] + 0.2 * df["attendance"]
               + rng.normal(0, 5, n)).clip(0, 100).round(1)
df.loc[rng.choice(n, 10, replace=False), "attendance"] = np.nan   # inject missing values
print(df.head())
print("\ninfo:"); df.info()
print("\ndescribe:\n", df.describe().round(2))
print("\nmissing values:\n", df.isnull().sum())
df["attendance"] = df["attendance"].fillna(df["attendance"].mean())
print("\nGroup mean marks by branch:\n", df.groupby("branch")["marks"].mean().round(2))
print("\nFilter marks>80 count:", (df["marks"] > 80).sum())
print("\nPivot table:\n", df.pivot_table(values="marks", index="branch",
                                         columns="gender", aggfunc="mean").round(2))
df["grade"] = pd.cut(df["marks"], [0, 50, 65, 80, 100], labels=["D", "C", "B", "A"])
print("\nGrade counts:\n", df["grade"].value_counts())
df.to_csv("output/students.csv", index=False)

# ---------------- Matplotlib ----------------
print("\n" + "=" * 20, "MATPLOTLIB", "=" * 20)
fig, ax = plt.subplots(2, 2, figsize=(11, 8))
ax[0, 0].plot(np.sort(df["marks"].values)); ax[0, 0].set_title("Line: sorted marks")
ax[0, 1].scatter(df["study_hours"], df["marks"], alpha=.6, c="tab:green")
ax[0, 1].set(title="Scatter: hours vs marks", xlabel="hours", ylabel="marks")
ax[1, 0].hist(df["marks"], bins=15, color="tab:orange", edgecolor="k"); ax[1, 0].set_title("Histogram")
df.groupby("branch")["marks"].mean().plot(kind="bar", ax=ax[1, 1], color="tab:purple")
ax[1, 1].set_title("Bar: mean marks by branch")
plt.tight_layout(); plt.savefig("output/exp1_matplotlib.png", dpi=120); plt.close()

# ---------------- Seaborn ----------------
print("\n" + "=" * 20, "SEABORN", "=" * 20)
fig, ax = plt.subplots(2, 2, figsize=(11, 8))
sns.histplot(df["marks"], kde=True, ax=ax[0, 0]); ax[0, 0].set_title("Histplot + KDE")
sns.boxplot(x="branch", y="marks", data=df, ax=ax[0, 1]); ax[0, 1].set_title("Boxplot")
sns.scatterplot(x="study_hours", y="marks", hue="gender", data=df, ax=ax[1, 0]); ax[1, 0].set_title("Scatter by gender")
sns.heatmap(df[["study_hours", "attendance", "marks"]].corr(), annot=True, cmap="coolwarm", ax=ax[1, 1])
ax[1, 1].set_title("Correlation heatmap")
plt.tight_layout(); plt.savefig("output/exp1_seaborn.png", dpi=120); plt.close()
sns.pairplot(df[["study_hours", "attendance", "marks"]]).savefig("output/exp1_pairplot.png")
print("Plots + students.csv saved in ./output")
