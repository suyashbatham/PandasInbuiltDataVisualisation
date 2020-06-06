import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

x2 = np.random.rand(10,5)
df4 = pd.DataFrame(x2,columns=['a','b','c','d','e'])
# df4.plot.hist()
# df4.hist()
# df4['d'].hist()

# df4.plot.bar()
#
# df4.plot.area(alpha=0.5)
#
# df4.plot(kind='hist')  # kind means providing specification like bar , hist


# df4.plot.box()

df4.plot.hexbin(x='a',y='b',gridsize=10)
plt.show()

