import pandas as pd
from pandas.io.pytables import performance_doc
lis=[1,2,3,4,5]
pan=pd.Series(lis)
print("List is :",lis)
print("Series :\n",pan)
print(type(pan))
pp=pd.Series()
print(type(pp))
