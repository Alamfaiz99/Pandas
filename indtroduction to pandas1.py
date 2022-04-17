import pandas as pd
'''
1)high performance data analysis tool

-->this can be implemented with the help of three datasets
1)Series()
----------
data is represented in one dimensional array
-->list as argument
syntax:
import pandas as pd
pd.Series(data,index)


2)Dataframe()--->most efficient to do the analysis on datasets
----------
data is represented in two dimensional array
-->list or dict or series or another data frame
pd.Dataframe(data,index)

3)Panel
--------
data is represented in multidimensional array
data,major axis-->column
minor axis-->rows
as argument

pd.Panel(data,major axis,minor axis)

2)working with large data set
3)supports or it can laod files with different formats
4)more flexible to use
5)data is  represented in tabular form
means rows and column
6)suitable for working with missing data
7)indexing,slicing,sub setting large data
8)we can merge or join two different dataset easily
9)we can also reshape the datasets

'''

l=[10,20,30,40]

s1=pd.Series(l)
print(s1)

s1=pd.Series(l,index=['i','ii','iii','iv'])
print(s1)
'''
index|data
0      10
1      20
2      30
3      40
dtype: int64
i      10
ii     20
iii    30
iv     40
dtype: int64
'''

d={'name':['faizan','faiz','alam','don'],'perc':[98,96,67,97]}
d1=pd.DataFrame(d)
print(d1)

'''
tabulart form-->frame data frame
index col1  col2
      name  perc
0    faizan   98<--rows
1     faiz    96
2     alam    67
3      don    97

'''
