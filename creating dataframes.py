import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df1 = sns.load_dataset('tips')
df2 = pd.read_csv('original')
print(df1)
print(df2)

x1 = np.random.rand(100,5)
x2 = np.random.rand(10,5)  # row,column
df3 = pd.DataFrame(x1,columns=['a','b','c','d','e'])
print(df3)
print("$"*88)
df4 = pd.DataFrame(x2,columns=['a','b','c','d','e'])
print(df4)
