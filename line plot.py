import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

x1 = np.random.rand(100,5)
df3 = pd.DataFrame(x1,columns=['a','b','c','d','e'])
# df3.plot.line()
# df3['c'].plot.line()  # particular column
# plt.show()

x2 = np.random.rand(10,5)
df4 = pd.DataFrame(x2,columns=['a','b','c','d','e'])
# df4.plot.line()
# df4.plot.kde()
df4.plot.density()  # same as kde plot
plt.show()