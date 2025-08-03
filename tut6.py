#csv(comma seperated value)
from io import StringIO,BytesIO
import pandas as pd
import numpy as np
#csv file to df.
data = ('col1,col2,col3\n'
        'x,y,1\n'
        'a,b,2\n'
        'c,d,3')
print(type(data))
print(pd.read_csv(StringIO(data)))
df=pd.read_csv(StringIO(data), usecols=['col1','col3'])#usecol will diplay only specific col
print(df)

#df to csv
df.to_csv('Test.csv')

print(df.dtypes)
data1 = ('index,a,b,c\n'
         '4,apple,bat\n'
         '8,orange,cow')
print(pd.read_csv(StringIO(data1)))
#but we want to to shift index to the left
print(pd.read_csv(StringIO(data1,index_col=0)))

data2 =('a,b,c\n'
        '4,apple,bat,\n'
        '8,orange,cow,')
print(pd.read_csv(StringIO(data2)))