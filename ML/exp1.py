import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data={
    'Student':['a','b','c','d','e'],
    'hours':['1','2','3','4','5'],
    'marks':['45','50','55','60','70']
}
df=pd.DataFrames(data)
print(df)
#Numpy
mean=np.mean(df['marks'])
median=np.median(df['marks'])
print(f"Mean : {mean}")
print(f"Median : {median}")

plt.plot(df["Hours"],df["marks"],marker="o")
plt.title("Hours vs Marks")
plt.xlabel("Hours")
plt.ylabel("Marks")
plt.show()

sns.boxplot(x=df["Marks"])
plt.title("Marks distribution")
plt.show()