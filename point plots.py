import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df1 = sns.load_dataset('tips')
print(df1.head())
df2 = pd.read_csv('original')
print(df2.head())
x1 = np.random.rand(100,5)
df3 = pd.DataFrame(x1,columns=['a','b','c','d','e'])
print(df3.head())
x2 = np.random.rand(10,5)
df4 = pd.DataFrame(x2,columns=['a','b','c','d','e'])
print(df4.head())

print(df3.plot.scatter(x='a',y='b'))
df4.plot.scatter(x='a',y='b')
plt.show()