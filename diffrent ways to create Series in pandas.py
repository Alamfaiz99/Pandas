import pandas as pd
import numpy as np
'''
different ways of creating series in pandas
1)empty Series
import pandas as pd
s=pd.Series()

2)creating series using arrays
import numpy as np

a=np.array([10,20,30,40])
s=pd.Series(a)

3)creating series using list
l=[10,20,30,40]
s=pd.Series(l)

4)creating series using dictionary
d={'name':['a','b','c'],'values':[10,20,30,40]}
s=pd.Series(d)

'''
# s0=pd.Series()
# print(s0)
sl=pd.Series([10,20,30,40],index=['a','b','c','d'])
print(sl)

a=np.array([10,20,30,40])
s1=pd.Series(a)
print(s1)
