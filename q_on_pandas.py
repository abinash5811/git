import pandas as pd
import numpy as np
# dict1={"name":['abinash','akash','malaya','snehasis'],
# "marks":[90,87,74,70],
# "city":['kendrapara','cuttack','bbsr','anugul']
# }

# df=pd.DataFrame(dict1)
# # print(df)
# df.head(2)
# print(df)
# ser=pd.Series(np.random.rand(34))
# # print(ser)

newdf=pd.DataFrame(np.random.rand(334,5),index=np.arange(334))
# newdf.head(5)
print(newdf.tail(5))
print(newdf.describe())
print(newdf.index)
print(newdf.columns)