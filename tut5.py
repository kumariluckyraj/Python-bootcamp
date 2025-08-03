import pandas as pd
import numpy as np

df= pd.DataFrame(np.arange(0,20).reshape(5,4),index=['row1','row2','row3','row4','row5'],columns=['col1','col2','col3','col4'])
print(df.head())#random no.b/w 0 to 20
print(df.loc['row1'])#series
print(type(df.loc['row1']))#it is dataseries(1col or row)
print(df.iloc[0:2,0:2])#it's type is dataframe

#df to array
print(df.iloc[:,:].values)
df.isnull().sum()#check if the value is null or not , if not then the output will be 0 
df.describe #characters are ignored and only int and float values are taken
print(df.info)

test_df=pd.read_csv('test1.csv')
print(test_df)

print(df['col1'][1])#output is 4