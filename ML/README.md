# Machine Learning Lab - Practical Solutions

| # | File | Topic |
|---|------|-------|
| 1 | exp01_python_libraries.py | NumPy, Pandas, Matplotlib, Seaborn |
| 2 | exp02_regression.py | Simple, Multiple, Logistic Regression + metrics |
| 3 | exp03_decision_tree.py | Decision Tree (classification & regression) |
| 4 | exp04_svm.py | SVM: classification, regression (SVR), outlier detection |
| 5 | exp05_adaboost_xgboost.py | AdaBoost & XGBoost |
| 6 | exp06_kmeans.py | K-Means clustering (elbow, silhouette) |
| 7 | exp07_pca.py | PCA dimensionality reduction |
| 8 | exp08_reinforcement_learning.py | Q-Learning on a grid world |
| 9 | exp09_hyperparameter_tuning.py | GridSearchCV / RandomizedSearchCV |

## Run
    pip install -r requirements.txt
    python exp01_python_libraries.py      # one experiment
    python run_all.py                     # all experiments

Every program creates its own dataset (saved as CSV) and saves plots/CSVs in `./output`.
To view plots in a window instead, delete the line `matplotlib.use("Agg")`.
