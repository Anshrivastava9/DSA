import numpy as np
import pandas as pd

d={'A':[1,2,3,np.nan],'B':[5,2,np.nan,np.nan],'C':[1,2,3,4]}
df=pd.DataFrame(d)
#print(df)   

df.dropna()
#print(df.dropna())
#print(df.dropna(axis=1))

df.dropna(thresh=2)# this prints rows having at least 2 non-zero value

g=df.fillna(value='FILL VALUE')
#print(g)

f=df['A'].fillna(value=df['A'].mean())
#print(f)
list2='7 5 6'.split()

#df.loc[4]=list2
#print(df)

d=df['A'].fillna(value=df['A'].mean())
#print(d)
