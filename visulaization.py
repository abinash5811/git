# import matplotlib.pyplot as plt
# import numpy as np
# x=np.linspace(10,100,10)
# y=np.sin(x)
# plt.plot(x,y,color='green',linewidth=1)
# plt.scatter(x, y)
# plt.show()

import pandas as pd 
df = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8]}) 
print(df)
print(df.mean())