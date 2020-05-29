import numpy as ns
from numpy.random import randn
import pandas as pd

ns.random.seed(1)
df=pd.DataFrame(randn(5,4),['A','B','C','D','E'],['P','Q','R','S'])
#print(df)

reset_indexing_table=df.reset_index()
#print(reset_indexing_table)

new_col='Delhi Mumbai kolkata Chennai Hyderabad'.split()
df['Cities']=new_col
#print(df)

df.reset_index(inplace=True)
df.set_index('Cities',inplace=True)
#print(df)

#-------------------------Advance things
indexes=['G1','G1','G1','G2','G2','G2']
levels=[1,2,3,1,2,3]
hier_index=list(zip(indexes,levels))
hier_index=pd.MultiIndex.from_tuples(hier_index)

#print(hier_index)
df=pd.DataFrame(randn(6,2),hier_index,['P','Q'])
#print(df)
df.index.names=['Num1','Num2']
#print(df)
ast=df.xs(2,level='Num2')
print(ast)



#-----------------FINISH

